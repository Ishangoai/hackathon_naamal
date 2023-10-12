import models, schema
from sqlalchemy.orm import Session

def get_alumni_data(db: Session):
  """
  Get all Alumni from database
  """
  return db.query(models.Alumni).all()

def get_alumni_by_email(email, db: Session):
  """
  Get alumni by email
  """
  return db.query(models.Alumni).get(email)