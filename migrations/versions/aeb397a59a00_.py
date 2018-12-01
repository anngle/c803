"""empty message

Revision ID: aeb397a59a00
Revises: e26e661a9b9e
Create Date: 2018-11-16 22:09:08.821194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeb397a59a00'
down_revision = 'e26e661a9b9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.String(length=80), nullable=False),
    sa.Column('earnings', sa.String(length=80), nullable=0),
    sa.Column('cycle', sa.Integer(), nullable=True),
    sa.Column('enable', sa.Boolean(), nullable=True),
    sa.Column('product_sum', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('system_config', sa.Column('default_send_product', sa.Integer(), nullable=True))
    op.add_column('system_config', sa.Column('max_buy_product', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('system_config', 'max_buy_product')
    op.drop_column('system_config', 'default_send_product')
    op.drop_table('products')
    # ### end Alembic commands ###
