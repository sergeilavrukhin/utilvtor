"""empty message

Revision ID: 54d4616b0778
Revises: d08e9bd999e2
Create Date: 2020-12-24 01:43:20.409699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d4616b0778'
down_revision = 'd08e9bd999e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('queries', sa.Column('date_create', sa.DateTime(), nullable=True))
    op.drop_column('queries', 'region')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('queries', sa.Column('region', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('queries', 'date_create')
    # ### end Alembic commands ###
