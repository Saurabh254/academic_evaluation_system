from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    name: Optional[str]  # Name is nullable as per the SQLAlchemy model
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]
    father_name: Optional[str]
    mother_name: Optional[str]
    semester: int = 1
    active: bool = True
    dob: Optional[datetime]

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    password: str  # Password is required for creation


class StudentProfile(StudentBase):
    id: str
    created_at: datetime
    updated_at: datetime


class LoginResponse(BaseModel):
    access_token: str
    student: StudentProfile
