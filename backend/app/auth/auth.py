from datetime import datetime, timedelta
from typing import Annotated, Any, Literal, Optional, Union

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth_bearer import JWTBearer
from app.database.db import get_async_db
from app.exceptions import UnauthorisedUser
from app.students import models as student_models
from app.teachers import models as teacher_models
from jose import JWTError, jwt
from app.students import interface as student_interface
from app.teachers import interface as teacher_interface

SECRET_KEY = "8cbfecba4cd7d500fdd63917cbe3ce517f0d72946d9e9f7f5e7820d74fb38082"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30


def is_student(user: Union[student_models.Student, teacher_models.Teacher]) -> bool:
    return isinstance(user, student_models.Student)


def is_teacher(user: Union[student_models.Student, teacher_models.Teacher]) -> bool:
    return isinstance(user, teacher_models.Teacher)


def get_user_type(user: Union[student_models.Student, teacher_models.Teacher]) -> str:
    type = None
    if isinstance(user, student_models.Student):
        type = "Student"
    elif isinstance(user, teacher_models.Teacher):
        type = "Teacher"

    return type


def create_access_token(
    user: Union[student_models.Student, teacher_models.Teacher],
    expires_delta: Union[timedelta, None] = None,
) -> str:
    to_encode = {"id": user.id, "role": get_user_type(user)}

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})  # type: ignore
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decrypt_access_token(token: str, role: Literal["Student", "Teacher"]) -> str:
    user_id = None  # type: ignore
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")  # type: ignore
        _role: str = payload.get("role")  # type: ignore
        if _role != role:
            raise
    except (JWTError, Exception):
        pass
    return user_id


async def get_optional_loggedin_user(
    token: Annotated[str, Depends(JWTBearer(auto_error=False))],
    session: AsyncSession = Depends(get_async_db),
) -> Union[student_models.Student, teacher_models.Teacher, None]:
    user_id = None  # type: ignore
    role = None  # type: ignore
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")  # type: ignore
        role: str = payload.get("role")  # type: ignore
    except (JWTError, Exception):
        pass
    user = None
    if user_id:
        if role == "Student":
            user = await student_interface.get_student(
                student_id=user_id, session=session
            )
        elif role == "Teacher":
            user = await teacher_interface.get_teacher(
                teacher_id=user_id, session=session
            )
    return user


async def get_loggedin_user(
    optional_user: Annotated[
        Optional[Union[student_models.Student, teacher_models.Teacher]],
        Depends(get_optional_loggedin_user),
    ]
) -> Union[student_models.Student, teacher_models.Teacher]:

    if optional_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return optional_user


async def get_current_user(
    loggedin_user: Annotated[
        student_models.Student | teacher_models.Teacher | None,
        Depends(get_loggedin_user),
    ],
) -> student_models.Student:

    if is_student(loggedin_user):
        return loggedin_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized."
        )


async def get_current_active_user(
    user: Any = Depends(get_current_user),
) -> student_models.Student:
    if user.active:
        return user
    raise UnauthorisedUser(message="forbidden user")


async def get_current_teacher(
    loggedin_user: Annotated[
        student_models.Student | teacher_models.Teacher | None,
        Depends(get_loggedin_user),
    ],
) -> teacher_models.Teacher:
    if is_teacher(loggedin_user):
        return loggedin_user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized."
        )


async def get_user_from_access_token(
    token: str, session: AsyncSession
) -> student_models.Student | teacher_models.Teacher:
    user_id = None  # type: ignore
    role = None  # type: ignore
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")  # type: ignore
        role: str = payload.get("role")  # type: ignore

    except (JWTError, Exception):
        pass
    if role == "Teacher":
        return await teacher_interface.get_teacher(teacher_id=user_id, session=session)
    elif role == "Student":
        return await student_interface.get_student(student_id=user_id, session=session)
    else:
        raise
