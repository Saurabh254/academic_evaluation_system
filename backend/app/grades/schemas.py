# app/grades/schemas.py
from pydantic import BaseModel
from typing import Any, ClassVar, Dict
from datetime import datetime

from app.students.schemas import StudentProfile


class GradeCreate(BaseModel):
    subject: str
    marks: str


class StudentGradeCreate(BaseModel):
    subject: list[
        GradeCreate
    ]  # dictionary where the key is the subject and value is the grade (e.g. {"math": "A", "science": "B+"})
    cgpa: float  # CGPA (0-10 scale)
    semester: int

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models


class Grades(BaseModel):
    subject: str
    marks: str


class StudentGrade(BaseModel):
    id: str  # Grade entry ID
    grades: list[Grades]
    student_id: str  # Student ID
    created_at: datetime  # Timestamp when the grade was created
    updated_at: datetime  # Timestamp when the grade was last updated
    cgpa: float  # CGPA (0-10 scale)
    semester: int

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models


class StudentGradeResponse(BaseModel):
    student: StudentProfile
    grades: list[StudentGrade]
