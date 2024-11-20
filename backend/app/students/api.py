from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import auth
from app.database.db import get_async_db
from app.teachers import models as teacher_models
from . import interface, models, schemas

router = APIRouter(tags=["student"], prefix="/students")


@router.post(
    "/login",
    description="Log in the user with a phone number and OTP to get an access token.",
    response_model=schemas.LoginResponse,
)
async def login(
    username: str = Body(..., description="User's enrollment number"),
    password: str = Body(..., description="users password"),
    db: AsyncSession = Depends(get_async_db),
):
    return await interface.login_student(username, password, db)


@router.post(
    "/signup",
    description="Sign up a new user using the provided data.",
    response_model=schemas.StudentProfile,
)
async def signup(
    user_data: schemas.StudentCreate, db: AsyncSession = Depends(get_async_db)
):
    return await interface.signup_student(user_data, session=db)


@router.post(
    "/logout",
    description="Logs out the currently authenticated user and invalidates the session.",
)
async def logout(current_user: models.Student = Depends(auth.get_current_active_user)):
    return await interface.logout_student(current_user)


@router.get(
    "/all",
)
async def list_students(
    current_user: teacher_models.Teacher = Depends(auth.get_current_teacher),
    db: AsyncSession = Depends(get_async_db),
):
    ...
    return await interface.list_students(db)


@router.get(
    "/me",
    response_model=schemas.StudentProfile,
    description="Retrieve the profile of the currently authenticated user.",
)
async def read_me(current_user: models.Student = Depends(auth.get_current_active_user)):
    return current_user


@router.get("/{student_id}", dependencies=[Depends(auth.get_current_teacher)])
async def get_student_by_id(
    student_id: str, session: AsyncSession = Depends(get_async_db)
):
    return await interface.get_student(student_id, session)
