from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Date

from app.database.mixins import BaseModel


class Teacher(BaseModel):
    __tablename__ = "teachers"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(15), nullable=True)
    date_of_birth: Mapped[Date | None] = mapped_column(Date, nullable=True)
    subject: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[str] = mapped_column(String(100), nullable=False)
    joining_date: Mapped[Date] = mapped_column(Date, nullable=False)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<Teacher(id={self.id}, unique_id={self.unique_id}, name={self.name}, email={self.email})>"
