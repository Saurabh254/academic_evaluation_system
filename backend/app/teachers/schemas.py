from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class TeacherBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    subject: str
    department: str
    joining_date: date
    address: Optional[str] = None


class TeacherCreate(TeacherBase):
    password: str


class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    subject: Optional[str] = None
    department: Optional[str] = None
    joining_date: Optional[date] = None
    address: Optional[str] = None
    password: Optional[str] = None


class TeacherResponse(TeacherBase):
    id: str

    class Config:
        orm_mode = True
