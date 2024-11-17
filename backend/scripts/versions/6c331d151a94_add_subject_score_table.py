"""add subject score table

Revision ID: 6c331d151a94
Revises: 84ec7504a4d5
Create Date: 2024-11-17 22:53:09.395621

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "6c331d151a94"
down_revision: Union[str, None] = "84ec7504a4d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "student_grades",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.create_table(
        "student_subject_score",
        sa.Column("subject", sa.String(), nullable=False),
        sa.Column("marks", sa.String(), nullable=False),
        sa.Column("student_grades", sa.String(), nullable=False),
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["student_grades"],
            ["student_grades.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_student_subject_score_created_at"),
        "student_subject_score",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_student_subject_score_id"),
        "student_subject_score",
        ["id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_student_subject_score_updated_at"),
        "student_subject_score",
        ["updated_at"],
        unique=False,
    )
    op.alter_column(
        "student_grades",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
    )
    op.alter_column(
        "student_grades",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
    )
    op.create_index(
        op.f("ix_student_grades_created_at"),
        "student_grades",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_student_grades_id"), "student_grades", ["id"], unique=False
    )
    op.create_index(
        op.f("ix_student_grades_updated_at"),
        "student_grades",
        ["updated_at"],
        unique=False,
    )
    op.drop_column("student_grades", "subject")
    op.alter_column(
        "students",
        "dob",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "students",
        "dob",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=True,
    )
    op.add_column(
        "student_grades",
        sa.Column(
            "subject",
            postgresql.JSONB(astext_type=sa.Text()),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_index(op.f("ix_student_grades_updated_at"), table_name="student_grades")
    op.drop_index(op.f("ix_student_grades_id"), table_name="student_grades")
    op.drop_index(op.f("ix_student_grades_created_at"), table_name="student_grades")
    op.alter_column(
        "student_grades",
        "updated_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
    )
    op.alter_column(
        "student_grades",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
    )
    op.alter_column(
        "student_grades",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.drop_index(
        op.f("ix_student_subject_score_updated_at"), table_name="student_subject_score"
    )
    op.drop_index(
        op.f("ix_student_subject_score_id"), table_name="student_subject_score"
    )
    op.drop_index(
        op.f("ix_student_subject_score_created_at"), table_name="student_subject_score"
    )
    op.drop_table("student_subject_score")
    # ### end Alembic commands ###