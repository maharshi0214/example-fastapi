"""add content column to posts table 

Revision ID: abb97e758bb8
Revises: 5c5d7e4ac6ec
Create Date: 2026-06-29 13:32:47.666421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abb97e758bb8'
down_revision: Union[str, Sequence[str], None] = '5c5d7e4ac6ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
