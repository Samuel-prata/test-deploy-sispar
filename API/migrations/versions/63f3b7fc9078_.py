"""empty message

Revision ID: 63f3b7fc9078
Revises: 45562611da39
Create Date: 2025-01-06 17:32:43.704628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63f3b7fc9078'
down_revision = '45562611da39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refund',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('reason', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refund')
    # ### end Alembic commands ###
