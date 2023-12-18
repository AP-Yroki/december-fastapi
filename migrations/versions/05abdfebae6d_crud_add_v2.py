"""crud add-v2

Revision ID: 05abdfebae6d
Revises: 3de2f2343871
Create Date: 2023-12-17 22:27:15.562276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05abdfebae6d'
down_revision: Union[str, None] = '3de2f2343871'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('tech_type', sa.String(), nullable=True),
    sa.Column('tech_variation', sa.String(), nullable=True),
    sa.Column('manufacturer', sa.String(), nullable=True),
    sa.Column('product_characteristics', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('availability', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_product_name'), 'product', ['product_name'], unique=False)
    op.drop_index('ix_products_product_name', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tech_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tech_variation', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('manufacturer', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('product_characteristics', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('availability', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('photo_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    op.create_index('ix_products_product_name', 'products', ['product_name'], unique=False)
    op.drop_index(op.f('ix_product_product_name'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
