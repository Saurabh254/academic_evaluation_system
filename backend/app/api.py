from fastapi import APIRouter

from app.students import api as student_api
from app.teachers import api as teacher_api
from app.grades import api as grades_api

router = APIRouter(prefix="/api/v1")

router.include_router(student_api.router)
router.include_router(teacher_api.router)
router.include_router(grades_api.router)
