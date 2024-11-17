# app/interface/grades.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.grades.models import StudentGrade, StudentSubjectScore
from app.students.models import Student
from app.teachers.models import Teacher
from fastapi import HTTPException


async def add_grade(
    student_id: str, grade_data: dict, current_user: Teacher, session: AsyncSession
):
    """
    Adds grades for a student. Only a teacher can add grades.
    """
    # Verify the user is a teacher
    if not isinstance(current_user, Teacher):
        raise HTTPException(status_code=403, detail="Only teachers can add grades")

    # Check if the student exists
    stmt = select(Student).filter(Student.id == student_id)
    result = await session.execute(stmt)
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # Create a new grade record
    student_grade = StudentGrade(
        student_id=student_id,
        semester=grade_data.get("semester"),
        cgpa=grade_data.get("cgpa", 0),
    )
    session.add(student_grade)
    await session.commit()
    await session.refresh(student_grade)

    for sub in grade_data.get("subject", []):

        grade = StudentSubjectScore(
            subject=sub.get("subject"),
            marks=sub.get("marks"),
            student_grades_id=student_grade.id,
        )
        session.add(grade)
    await session.commit()


async def get_grades(student_id: str, session: AsyncSession):

    subq = select(StudentGrade.id.label("student_id")).filter(
        StudentGrade.student_id == student_id
    )
    stmt = (
        select(StudentGrade)
        .options(joinedload(StudentGrade.grades))
        .filter(StudentGrade.id == subq.c.student_id)
    )
    result = await session.execute(stmt)
    grades = result.unique().fetchall()
    if not grades:
        raise HTTPException(status_code=404, detail="No grades found for this student")

    return {"k": grades}


async def get_grade(current_user: Student, session: AsyncSession):
    """
    Fetches grades for the logged-in student.
    """
    subq = select(StudentGrade.id.label("student_id")).filter(
        StudentGrade.student_id == current_user.id
    )
    stmt = (
        select(StudentGrade)
        .options(joinedload(StudentGrade.grades))
        .filter(StudentGrade.id == subq.c.student_id)
    )
    result = await session.execute(stmt)
    grades = result.unique().fetchone()
    print(grades)
    if not grades:
        raise HTTPException(status_code=404, detail="No grades found for this student")

    return grades
