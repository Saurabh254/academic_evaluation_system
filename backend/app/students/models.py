from io import BytesIO
from nanoid import generate
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.mixins import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, nullable=True)
    enrollment: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, default=lambda: generate(size=12)
    )
    password: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    father_name: Mapped[str] = mapped_column(String, nullable=True)
    mother_name: Mapped[str] = mapped_column(String, nullable=True)
    dob: Mapped[str] = mapped_column(DateTime, nullable=True)

    def __repr__(self):
        return f"<User(name='{self.name}', active={self.active})>"
