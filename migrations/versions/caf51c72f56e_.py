"""empty message

Revision ID: caf51c72f56e
Revises: 
Create Date: 2024-02-12 18:08:52.187223

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'caf51c72f56e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('firm_data',
    sa.Column('firm_id', sa.Integer(), nullable=False),
    sa.Column('firm_name', sa.String(length=30), nullable=True),
    sa.Column('firm_link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('firm_id')
    )
    with op.batch_alter_table('stock_data', schema=None) as batch_op:
        batch_op.alter_column('stock_name',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=100),
               nullable=True)
        batch_op.alter_column('trading_firm',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_data', schema=None) as batch_op:
        batch_op.alter_column('trading_firm',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.alter_column('stock_name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=30),
               nullable=False)

    op.drop_table('firm_data')
    # ### end Alembic commands ###
