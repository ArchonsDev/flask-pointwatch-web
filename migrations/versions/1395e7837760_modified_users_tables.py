"""modified users tables

Revision ID: 1395e7837760
Revises: 
Create Date: 2024-04-10 00:56:56.031925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1395e7837760'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.String(length=255), nullable=False))
        batch_op.alter_column('id',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.create_unique_constraint(None, ['employee_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False,
               autoincrement=True)
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
