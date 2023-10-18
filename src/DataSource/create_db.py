from sqlalchemy import create_engine, Column, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from decouple import config
from cleaning_utils import data_types
from passlib.context import CryptContext
class Base(DeclarativeBase):
    pass


class Alumni(Base):
    __tablename__ = 'alumni'

    timestamp = Column(data_types['timestamp'])
    email = Column(data_types['email'], primary_key=True)
    first_name = Column(data_types['first_name'])
    last_name = Column(data_types['last_name'])
    phone_number = Column(data_types['phone_number'])
    location_city = Column(data_types['location_city'])
    location_country = Column(data_types['location_country'])
    nationality = Column(data_types['nationality'])
    right_to_work = Column(data_types['right_to_work'])
    id_documents = Column(data_types['id_documents'])
    has_bank_account = Column(data_types['has_bank_account'])
    bank_account_registered_in_country = Column(data_types['bank_account_registered_in_country'])
    receive_payments_abroad = Column(data_types['receive_payments_abroad'])
    linkedin_profile = Column(data_types['linkedin_profile'])
    github_profile = Column(data_types['github_profile'])
    cv_link = Column(data_types['cv_link'])
    personal_website = Column(data_types['personal_website'])
    skills_react = Column(data_types['skills_react'])
    skills_python = Column(data_types['skills_python'])
    skills_css = Column(data_types['skills_css'])
    skills_javascript = Column(data_types['skills_javascript'])
    skills_html = Column(data_types['skills_html'])
    work_preference_remote = Column(data_types['work_preference_remote'])
    work_preference_colocated = Column(data_types['work_preference_colocated'])
    work_preference_hybrid = Column(data_types['work_preference_hybrid'])
    experience_years_colocated = Column(data_types['experience_years_colocated'])
    experience_years_remote = Column(data_types['experience_years_remote'])
    experience_years_hybrid = Column(data_types['experience_years_hybrid'])
    has_computer_access = Column(data_types['has_computer_access'])
    has_reliable_internet = Column(data_types['has_reliable_internet'])
    has_smartphone = Column(data_types['has_smartphone'])
    has_unlimited_mobile_data = Column(data_types['has_unlimited_mobile_data'])
    additional_information_for_employers = Column(data_types['additional_information_for_employers'])
    additional_information_for_naamal = Column(data_types['additional_information_for_naamal'])

# the database model for users
class Users(Base):
    __tablename__ = "users"

    username = Column(Text, primary_key=True)
    full_name = Column(Text)
    email = Column(Text)
    hashed_password = Column(Text)
    disabled = Column(Text)






db_url = config('DATABASE_URL')
engine = create_engine(db_url, echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password = pwd_context.hash("ishango")
password2 = pwd_context.hash("naamal")

Session = sessionmaker(bind=engine)
session = Session()

user1 = Users(username="dev", full_name="Ishango", email="dev@gmail.com", hashed_password=password, disabled=False)
user2 = Users(username="naamal", full_name="Naamal", email="naamal@gmail.com", hashed_password=password2, disabled=False)


session.add(user1)
session.add(user2)

session.commit()


