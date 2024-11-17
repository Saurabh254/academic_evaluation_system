"""change column type subject

Revision ID: c455ac79afef
Revises: 7589e570bb7a
Create Date: 2024-11-17 21:02:11.612959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c455ac79afef'
down_revision: Union[str, None] = '7589e570bb7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
