"""remove unique type from student_id

Revision ID: d4f4a706d064
Revises: 78a8c9a94989
Create Date: 2024-11-20 01:04:11.856491

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d4f4a706d064"
down_revision: Union[str, None] = "78a8c9a94989"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "student_grades_student_id_key", "student_grades", type_="unique"
    )
    op.create_unique_constraint(
        "uq_student_semester", "student_grades", ["student_id", "semester"]
    )


def downgrade() -> None:
    op.drop_constraint("uq_student_semester", "student_grades", type_="unique")
    op.create_unique_constraint(
        "student_grades_student_id_key", "student_grades", ["student_id"]
    )
