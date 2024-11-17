from datetime import datetime
from nanoid import generate
from sqlalchemy import DATETIME, Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.mixins import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    name: Mapped[str] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    semester: Mapped[int] = mapped_column(Integer, default=1)
    address: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    father_name: Mapped[str] = mapped_column(String, nullable=True)
    mother_name: Mapped[str] = mapped_column(String, nullable=True)
    dob: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(name='{self.name}', active={self.active})>"
