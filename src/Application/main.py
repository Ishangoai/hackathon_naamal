from typing import List
import service, models, schema
from database import SessionLocal,engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Na'amal Alumni API",
    description="API for retrieving information about Na'amal Alumni",
    docs_url="/"
)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/alumni", response_model=List[schema.AlumniModel])
def read_alumni_data(db: Session = Depends(get_db)) -> List[schema.AlumniModel]:
    """API endpoint for retrieving all alumni

    Args:
        no args

    Returns:
        The retrieved alumni
    """
    alumni_data = service.get_alumni_data(db)
    return alumni_data

@app.get("/alumni/{email}", response_model=schema.AlumniModel)
def get_alumni_by_email(email, db: Session = Depends(get_db)) -> schema.AlumniModel:
    """API endpoint for retrieving a alumni by email

    Args:
        email (str): the email of the alumni to retrieve

    Returns:
        dict: The retrieved alumni
    """
    alumni = service.get_alumni_by_email(email, db)

    return alumni