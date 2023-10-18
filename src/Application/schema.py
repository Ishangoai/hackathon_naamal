from typing import Optional
from pydantic import BaseModel, ConfigDict

# schema for returning an alumni
class AlumniModel(BaseModel):
    timestamp: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    location_city: Optional[str]
    location_country: Optional[str]
    nationality: Optional[str]
    right_to_work: Optional[str]
    id_documents: Optional[str]
    has_bank_account: Optional[str]
    bank_account_registered_in_country: Optional[str]
    receive_payments_abroad: Optional[str]
    linkedin_profile: Optional[str]
    github_profile: Optional[str]
    cv_link: Optional[str]
    personal_website: Optional[str]
    skills_react: Optional[str]
    skills_python: Optional[str]
    skills_css: Optional[str]
    skills_javascript: Optional[str]
    skills_html: Optional[str]
    work_preference_remote: Optional[str]
    work_preference_colocated: Optional[str]
    work_preference_hybrid: Optional[str]
    experience_years_colocated: Optional[str]
    experience_years_remote: Optional[str]
    experience_years_hybrid: Optional[str]
    has_computer_access: Optional[str]
    has_reliable_internet: Optional[str]
    has_smartphone: Optional[str]
    has_unlimited_mobile_data: Optional[str]
    additional_information_for_employers: Optional[str]

    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str