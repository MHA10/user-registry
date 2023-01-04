"""Initial migration.

Revision ID: 3e16cbf1dc97
Revises: 
Create Date: 2023-01-01 16:14:44.727421

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa

from app import db
from app.models.domainCheck import ListType

# revision identifiers, used by Alembic.
revision = '3e16cbf1dc97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('domaincheck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('belongs_to', sqlalchemy_utils.types.choice.ChoiceType(ListType, impl=db.String()), nullable=True),
    sa.Column('domain', sa.String(), nullable=True),
    sa.Column('authority_token', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_num', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('discoverable', sa.Boolean(), nullable=True),
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['domain_id'], ['domaincheck.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('domaincheck')
    op.drop_table('blacklist')
    # ### end Alembic commands ###