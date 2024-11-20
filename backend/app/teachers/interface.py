from typing import Sequence
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.teachers.models import Teacher
from app.teachers.schemas import TeacherCreate, TeacherUpdate
from app.auth import auth


async def create_teacher(session: AsyncSession, teacher_data: TeacherCreate) -> Teacher:
    teacher = Teacher(**teacher_data.dict())
    session.add(teacher)
    await session.commit()
    await session.refresh(teacher)
    return teacher


async def get_teacher(session: AsyncSession, teacher_id: str) -> Teacher | None:
    result = await session.execute(select(Teacher).where(Teacher.id == teacher_id))
    return result.scalar_one_or_none()


async def update_teacher(
    session: AsyncSession, teacher_id: str, teacher_data: TeacherUpdate
) -> Teacher | None:
    result = await session.execute(select(Teacher).where(Teacher.id == teacher_id))
    teacher = result.scalar_one_or_none()
    if teacher:
        for key, value in teacher_data.dict(exclude_unset=True).items():
            setattr(teacher, key, value)
        await session.commit()
        await session.refresh(teacher)
    return teacher


async def delete_teacher(session: AsyncSession, teacher_id: str) -> bool:
    result = await session.execute(select(Teacher).where(Teacher.id == teacher_id))
    teacher = result.scalar_one_or_none()
    if teacher:
        await session.delete(teacher)
        await session.commit()
        return True
    return False


async def get_all_teachers(
    session: AsyncSession, department: str | None = None, subject: str | None = None
) -> Sequence[Teacher]:
    query = select(Teacher)
    if department:
        query = query.where(Teacher.department == department)
    if subject:
        query = query.where(Teacher.subject == subject)
    result = await session.execute(query)
    return result.scalars().all()


async def authenticate_teacher(
    session: AsyncSession, username: str, password: str
) -> dict:
    result = await session.execute(select(Teacher).where(Teacher.id == username))
    teacher = result.scalar_one_or_none()
    if (
        not teacher or not teacher.password == password
    ):  # Replace with a secure password check
        raise HTTPException(status_code=404)

    access_token = auth.create_access_token(user=teacher)
    return {
        "access_token": access_token,
        "teacher": teacher.__dict__,
    }
