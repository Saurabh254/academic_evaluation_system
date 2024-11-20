from pydantic import BaseModel
from datetime import datetime


from app.students.schemas import StudentProfile


class Grade(BaseModel):
    subject: str
    marks: int


class StudentGradeCreate(BaseModel):
    subject: list[
        Grade
    ]  # dictionary where the key is the subject and value is the grade (e.g. {"math": "A", "science": "B+"})
    cgpa: float  # CGPA (0-10 scale)
    semester: int

    class Config:
        orm_mode = True  # Allows Pydantic to read data from SQLAlchemy models


class StudentGradeResponse(BaseModel):
    created_at: datetime
    updated_at: datetime
    semester: int
    cgpa: float
    grades: list[Grade]
