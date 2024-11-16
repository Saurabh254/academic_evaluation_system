from fastapi import APIRouter

from app.students import api as users_api

router = APIRouter(prefix="/api/v1")

router.include_router(users_api.router)
