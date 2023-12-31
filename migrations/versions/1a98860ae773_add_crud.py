"""add CRUD

Revision ID: 1a98860ae773
Revises: 0c86d05e984b
Create Date: 2023-12-17 00:09:54.473453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a98860ae773'
down_revision: Union[str, None] = '0c86d05e984b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('item_type', sa.String(), nullable=False),
    sa.Column('item_subtype', sa.String(), nullable=False),
    sa.Column('manufacturer', sa.String(), nullable=False),
    sa.Column('characteristics', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Integer(), nullable=False),
    sa.Column('photo_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
