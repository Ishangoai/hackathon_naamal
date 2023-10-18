from typing import List
from fastapi.security import OAuth2PasswordBearer
import service
from database import SessionLocal,engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import Base
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import SessionLocal
from schema import User, UserInDB, AlumniModel
from Hasher import Hasher

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Na'amal Alumni API",
    description="API for retrieving information about Na'amal Alumni",
    docs_url="/"
)

def toDict():
	users = service.get_users_data(db = SessionLocal())
	return {users[i].username: {"username": users[i].username, "hashed_password": users[i].hashed_password, "email": users[i].email, "disabled": users[i].disabled, "full_name": users[i].full_name} for i in range(0, len(users))}

users_dict = toDict()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def fake_decode_token(token):
    user = get_user(users_dict, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return {"username": current_user.username, "email": current_user.email, "full_name": current_user.full_name}

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """API endpoint for login

    Args:
        email (str): login data

    Returns:
        dict: The user and token bearer
    """
    user_dict = users_dict.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username")
    user = UserInDB(**user_dict)
    form_password = form_data.password
    if not Hasher.verify_password(form_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """API endpoint for retrieving current user

    Args:
        email (str): no args

    Returns:
        dict: The retrieved user
    """
    return current_user

@app.get("/alumni")
def read_alumni_data(
    alumni: Annotated[List[AlumniModel], Depends(get_current_active_user)]
) -> List[AlumniModel]:
    """API endpoint for retrieving all alumni

    Args:
        no args

    Returns:
        The retrieved alumni
    """
    db = SessionLocal()
    alumni_data = service.get_alumni_data(db)
    return alumni_data

@app.get("/alumni/{email}", response_model=AlumniModel)
def get_alumni_by_email(email, alumni: Annotated[List[AlumniModel], Depends(get_current_active_user)]
) -> AlumniModel:
    """API endpoint for retrieving a alumni by email

    Args:
        email (str): the email of the alumni to retrieve

    Returns:
        dict: The retrieved alumni
    """
    db = SessionLocal()
    alumni = service.get_alumni_by_email(email, db)
    return alumni

@app.patch("/users/{username}")
async def update_password(username: str, new_password: str, current_user: Annotated[User, Depends(get_current_user)]
):
    """Update user password by username

    Args:
        username (str): username of user to update
        password (str): new password for update

    Returns:
        dict: the updated success
    """
    db = SessionLocal()
    response = service.update_password(db, username, new_password)
    return response
   