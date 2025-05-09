"""migration refund

Revision ID: 4ad58c1bab96
Revises: 63f3b7fc9078
Create Date: 2025-02-25 17:29:24.456697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ad58c1bab96'
down_revision = '63f3b7fc9078'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('refund', schema=None) as batch_op:
        batch_op.add_column(sa.Column('colaborador', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('empresa', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('tipo_reembolso', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('centro_custo', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('ordem_interna', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('divisao', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('pep', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('moeda', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('valor', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('data', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('motivo', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('distancia_km', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('valor_km', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('valor_taxa', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('numero_prestacao_contas', sa.String(length=25), nullable=True))
        batch_op.drop_column('category')
        batch_op.drop_column('value')
        batch_op.drop_column('date')
        batch_op.drop_column('reason')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('refund', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reason', mysql.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('date', sa.DATE(), nullable=False))
        batch_op.add_column(sa.Column('value', mysql.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('category', mysql.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('numero_prestacao_contas')
        batch_op.drop_column('status')
        batch_op.drop_column('valor_taxa')
        batch_op.drop_column('valor_km')
        batch_op.drop_column('distancia_km')
        batch_op.drop_column('motivo')
        batch_op.drop_column('data')
        batch_op.drop_column('valor')
        batch_op.drop_column('moeda')
        batch_op.drop_column('pep')
        batch_op.drop_column('divisao')
        batch_op.drop_column('ordem_interna')
        batch_op.drop_column('centro_custo')
        batch_op.drop_column('tipo_reembolso')
        batch_op.drop_column('empresa')
        batch_op.drop_column('colaborador')

    # ### end Alembic commands ###
