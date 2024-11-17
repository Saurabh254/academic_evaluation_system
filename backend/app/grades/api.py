# app/routes/grades.py
import sched
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db import get_async_db
from app.auth import auth
from . import schemas
from .models import StudentGrade
from . import interface
from app.teachers.models import Teacher
from app.students.models import Student
from app.students import interface as student_interface

router = APIRouter(prefix="/grades", tags=["Grades"])


# Route for teachers to add grades for a student
@router.post(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def add_grade_for_student(
    student_id: str,
    grade_data: schemas.StudentGradeCreate,  # Example: {"subject": {"math": "A", "science": "B+"}, "cgpa": 8.5}
    current_user: Teacher = Depends(
        auth.get_current_teacher
    ),  # Ensure the current user is a teacher
    session: AsyncSession = Depends(get_async_db),
):
    await interface.add_grade(
        student_id, grade_data.model_dump(), current_user, session
    )


@router.get(
    "",
)
async def get_my_grades(
    current_user: Student = Depends(auth.get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    return await interface.get_grades(current_user.id, db)


# Route for students to view their grades
@router.get("/{student_id}", response_model=schemas.StudentGrade)
async def get_grades_for_student(
    student_id: str,
    current_user: Student = Depends(
        auth.get_current_teacher
    ),  # Ensure the current user is a student
    session: AsyncSession = Depends(get_async_db),
):
    return await interface.get_grades(student_id, session)
