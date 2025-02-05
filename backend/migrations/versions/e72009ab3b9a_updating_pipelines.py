"""create account table

Revision ID: e72009ab3b9a
Revises: 5e722995fa0b
Create Date: 2022-05-16 14:52:40.347079

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e72009ab3b9a'
down_revision = '5e722995fa0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('sqlpipeline', 'datapipeline')
    op.add_column(
        'datapipeline', sa.Column('devStrategy', sa.String(), nullable=True)
    )
    op.add_column(
        'datapipeline', sa.Column('devStages', postgresql.ARRAY(sa.String()), nullable=True)
    )
    op.alter_column(
        'datapipeline', 'sqlPipelineUri', new_column_name='DataPipelineUri'
    )
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datapipeline', 'devStrategy')
    op.drop_column('datapipeline', 'devStages')
    op.alter_column(
        'datapipeline', 'DataPipelineUri', new_column_name='sqlPipelineUri'
    )
    op.rename_table('datapipeline', 'sqlpipeline')
    # ### end Alembic commands ###
    pass
