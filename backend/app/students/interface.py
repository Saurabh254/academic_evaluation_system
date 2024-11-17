from typing import Any

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import auth
from app.exceptions import UnauthorisedUser

from . import errors, models, schemas


async def login_student(
    id: str, password: str, session: AsyncSession
) -> dict[str, Any]:
    stmt = select(models.Student).where(
        models.Student.id == id, models.Student.password == password
    )
    result = await session.execute(stmt)
    student = result.scalar_one_or_none()

    if not student:
        raise errors.StudentNotFound

    if not student.active:
        raise UnauthorisedUser

    access_token = auth.create_access_token(user=student)
    return {
        "access_token": access_token,
        "student": student.__dict__,
    }


async def signup_student(
    student_data: schemas.StudentCreate, session: AsyncSession
) -> models.Student:
    is_existing_stmt = (
        select(func.count())
        .select_from(models.Student)
        .filter(models.Student.phone == student_data.phone)
    )
    result = await session.execute(is_existing_stmt)
    count = result.scalar()
    if count:
        raise errors.StudentAlreadyExists

    student = models.Student(**student_data.model_dump(exclude={"otp"}))
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student


async def logout_student(student: models.Student) -> dict[str, str]:
    return {"msg": "Successfully logged out"}


async def get_student(student_id: str, session: AsyncSession) -> models.Student:
    stmt = select(models.Student).filter(models.Student.id == student_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
