from models import Alumni, Users
from sqlalchemy.orm import Session
from Hasher import Hasher

def get_alumni_data(db: Session):
  """
  Get all Alumni from database
  """
  return db.query(Alumni).all()

def get_alumni_by_email(email, db: Session):
  """
  Get alumni by email
  """
  return db.query(Alumni).get(email)

def get_users_data(db: Session):
  """
  Get all Alumni from database
  """
  return db.query(Users).all()

def get_user_by_username(username, db: Session):
  """
  Get user by username
  """
  return db.query(Users).get(username)

def update_password(
       db: Session , username, password
    ):
    """
      Update user by username
    """
    user_query = db.query(Users).filter(Users.username==username)
    user = user_query.first()
    if password:
        user.hashed_password = Hasher.get_password_hash(password)
    db.add(user)
    db.commit()
    return {"status": "successful"}