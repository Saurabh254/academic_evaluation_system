"""change subject type to list in grade table

Revision ID: 7589e570bb7a
Revises: 9f9231b82d5c
Create Date: 2024-11-17 20:50:26.573088

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

# revision identifiers, used by Alembic.
revision: str = "7589e570bb7a"
down_revision: Union[str, None] = "9f9231b82d5c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Alter the column to be an ARRAY of JSON
    op.drop_column(
        "student_grades",  # Table name
        "subject",  # Column name
    )
    op.add_column("student_grades", sa.Column("subject", ARRAY(JSONB)))


def downgrade():
    # Revert the column back to a single JSON type
    op.drop_column("student_grades", "subject")
    op.add_column(
        "student_grades",  # Table name
        sa.Column(
            "subject",  # Column name
            type_=sa.JSON(),  # Revert to the original JSON type
        ),
    )
