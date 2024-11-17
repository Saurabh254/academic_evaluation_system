from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.teachers.schemas import TeacherCreate, TeacherUpdate, TeacherResponse
from app.database.db import get_async_db
from app.teachers import (
    interface,
)  # Assuming your interface file is in the 'teacher' module

router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.post("/", response_model=TeacherResponse)
async def create_teacher_route(
    teacher_data: TeacherCreate, session: AsyncSession = Depends(get_async_db)
):
    return await interface.create_teacher(session, teacher_data)


@router.get("/{teacher_id}", response_model=TeacherResponse)
async def get_teacher_route(
    teacher_id: str, session: AsyncSession = Depends(get_async_db)
):
    teacher = await interface.get_teacher(session, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@router.put("/{teacher_id}", response_model=TeacherResponse)
async def update_teacher_route(
    teacher_id: str,
    teacher_data: TeacherUpdate,
    session: AsyncSession = Depends(get_async_db),
):
    updated_teacher = await interface.update_teacher(session, teacher_id, teacher_data)
    if not updated_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated_teacher


@router.delete("/{teacher_id}", response_model=dict)
async def delete_teacher_route(
    teacher_id: str, session: AsyncSession = Depends(get_async_db)
):
    success = await interface.delete_teacher(session, teacher_id)
    if not success:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return {"message": "Teacher deleted successfully"}


@router.get("/", response_model=list[TeacherResponse])
async def get_all_teachers_route(
    department: str | None = None,
    subject: str | None = None,
    session: AsyncSession = Depends(get_async_db),
):
    return await interface.get_all_teachers(session, department, subject)


@router.post("/login")
async def authenticate_teacher_route(
    email: str, password: str, session: AsyncSession = Depends(get_async_db)
):
    teacher = await interface.authenticate_teacher(session, email, password)
    if not teacher:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return teacher
