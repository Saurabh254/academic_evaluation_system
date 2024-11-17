"""change datetime column type

Revision ID: 0aa84042e7f4
Revises: c455ac79afef
Create Date: 2024-11-17 22:18:46.980653

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0aa84042e7f4"
down_revision: Union[str, None] = "c455ac79afef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.alter_column(
        "students",
        "dob",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "students",
        "dob",
        existing_type=sa.DateTime(),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=True,
    )

    # ### end Alembic commands ###
