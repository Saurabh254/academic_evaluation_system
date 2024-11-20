from sqlalchemy import ForeignKey, String, Integer, Float, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from app.database.mixins import (
    BaseModel,
)  # Assuming you have a BaseModel defined for your application
from app.students.models import Student


class StudentGrade(BaseModel):
    __tablename__ = "student_grades"

    student_id: Mapped[str] = mapped_column(
        String, ForeignKey("students.id"), nullable=False
    )
    cgpa: Mapped[float] = mapped_column(
        Float, nullable=False
    )  # Store CGPA as a float (0-10)
    semester: Mapped[int] = mapped_column(Integer, default=1)

    # Relationship to the Student model (assuming it exists)
    student: Mapped["Student"] = relationship("Student", backref="grades")
    grades: Mapped[list["StudentSubjectScore"]] = relationship(
        "StudentSubjectScore", uselist=True
    )
    __table_args__ = (
        UniqueConstraint(
            "student_id", "semester", name="uq_student_semester"
        ),  # Unique constraint
    )

    def __repr__(self) -> str:
        return f"<StudentGrade(student_id={self.student_id}, cgpa={self.cgpa})>"


class StudentSubjectScore(BaseModel):
    __tablename__ = "student_subject_score"
    subject: Mapped[str] = mapped_column(String, nullable=False)
    marks: Mapped[int] = mapped_column(Integer, nullable=False)
    student_grades_id: Mapped[StudentGrade] = mapped_column(
        String, ForeignKey("student_grades.id"), nullable=False
    )
