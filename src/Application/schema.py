from typing import Optional
from pydantic import BaseModel
from datetime import datetime,date

# schema for returning an alumni
class AlumniModel(BaseModel):
    timestamp: str
    email: str
    first_name: str
    last_name: str
    phone_number: str
    location_city: str
    location_country: str
    nationality: str
    right_to_work: str
    id_documents: str
    has_bank_account: str
    bank_account_registered_in_country: str
    receive_payments_abroad: str
    linkedin_profile: str
    github_profile: str
    cv_link: str
    personal_website: str
    skills_react: str
    skills_python: str
    skills_css: str
    skills_javascript: str
    skills_html: str
    work_preference_remote: str
    work_preference_colocated: str
    work_preference_hybrid: str
    experience_years_colocated: str
    experience_years_remote: str
    experience_years_hybrid: str
    has_computer_access: str
    has_reliable_internet: str
    has_smartphone: str
    has_unlimited_mobile_data: str
    additional_information_for_employers: str

    class Config:
        orm_mode = True