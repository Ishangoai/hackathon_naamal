from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime,Float,Text
from database import Base

# the database model for alumni
class Alumni(Base):
    __tablename__ = "alumni"

    timestamp = Column(Text)
    email = Column(Text, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    phone_number = Column(Text)
    location_city = Column(Text)
    location_country = Column(Text)
    nationality = Column(Text)
    right_to_work = Column(Text)
    id_documents = Column(Text)
    has_bank_account = Column(Text)
    bank_account_registered_in_country = Column(Text)
    receive_payments_abroad = Column(Text)
    linkedin_profile = Column(Text)
    github_profile = Column(Text)
    cv_link = Column(Text)
    personal_website = Column(Text)
    skills_react = Column(Text)
    skills_python = Column(Text)
    skills_css = Column(Text)
    skills_javascript = Column(Text)
    skills_html = Column(Text)
    work_preference_remote = Column(Text)
    work_preference_colocated = Column(Text)
    work_preference_hybrid = Column(Text)
    experience_years_colocated = Column(Text)
    experience_years_remote = Column(Text)
    experience_years_hybrid = Column(Text)
    has_computer_access = Column(Text)
    has_reliable_internet = Column(Text)
    has_smartphone = Column(Text)
    has_unlimited_mobile_data = Column(Text)
    additional_information_for_employers = Column(Text)

# the database model for users
class Users(Base):
    __tablename__ = "users"

    username = Column(Text, primary_key=True)
    full_name = Column(Text)
    email = Column(Text)
    hashed_password = Column(Text)
    disabled = Column(Text)
