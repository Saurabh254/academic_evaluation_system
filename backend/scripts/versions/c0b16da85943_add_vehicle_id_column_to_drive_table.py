"""add vehicle_id column to drive table

Revision ID: c0b16da85943
Revises: 9deece31c656
Create Date: 2024-10-17 16:41:02.198599

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0b16da85943"
down_revision: Union[str, None] = "9deece31c656"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column("drives", sa.Column("vehicle_id", sa.String(), nullable=False))

    op.create_foreign_key(None, "drives", "vehicle", ["vehicle_id"], ["id"])


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column("drives", "vehicle_id")
