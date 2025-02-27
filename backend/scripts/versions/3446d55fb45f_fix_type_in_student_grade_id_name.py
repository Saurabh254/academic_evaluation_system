"""fix_type in student grade id name

Revision ID: 3446d55fb45f
Revises: 6c331d151a94
Create Date: 2024-11-17 23:18:35.176804

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3446d55fb45f"
down_revision: Union[str, None] = "6c331d151a94"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "student_subject_score",
        sa.Column("student_grades_id", sa.String(), nullable=False),
    )
    op.drop_constraint(
        "student_subject_score_student_grades_fkey",
        "student_subject_score",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None, "student_subject_score", "student_grades", ["student_grades_id"], ["id"]
    )
    op.drop_column("student_subject_score", "student_grades")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "student_subject_score",
        sa.Column("student_grades", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(
        "student_subject_score_student_grades_fkey",
        "student_subject_score",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "student_subject_score_student_grades_fkey",
        "student_subject_score",
        "student_grades",
        ["student_grades"],
        ["id"],
    )
    op.drop_column("student_subject_score", "student_grades_id")
    # ### end Alembic commands ###
