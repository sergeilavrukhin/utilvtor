"""empty message

Revision ID: 3cb529f32591
Revises: 
Create Date: 2020-12-25 07:42:52.799833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cb529f32591'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aggregations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fkkoclass',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=600), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('query_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('middlename', sa.String(length=255), nullable=False),
    sa.Column('position', sa.String(length=255), nullable=True),
    sa.Column('itn', sa.String(length=12), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fkko',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('parent_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(length=600), nullable=False),
    sa.Column('fkkoclass_id', sa.Integer(), nullable=True),
    sa.Column('aggr_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aggr_id'], ['aggregations.id'], ),
    sa.ForeignKeyConstraint(['fkkoclass_id'], ['fkkoclass.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('queries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fkko_id', sa.BigInteger(), nullable=True),
    sa.Column('waste', sa.String(length=255), nullable=True),
    sa.Column('locality', sa.String(length=255), nullable=True),
    sa.Column('count', sa.Float(), nullable=True),
    sa.Column('date_create', sa.DateTime(), nullable=True),
    sa.Column('date_expiry', sa.DateTime(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('aggr_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('query_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aggr_id'], ['aggregations.id'], ),
    sa.ForeignKeyConstraint(['fkko_id'], ['fkko.id'], ),
    sa.ForeignKeyConstraint(['query_type_id'], ['query_type.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('queries')
    op.drop_table('fkko')
    op.drop_table('users')
    op.drop_table('units')
    op.drop_table('query_type')
    op.drop_table('fkkoclass')
    op.drop_table('aggregations')
    # ### end Alembic commands ###