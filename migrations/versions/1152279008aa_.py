"""empty message

Revision ID: 1152279008aa
Revises: 89ee48680e79
Create Date: 2019-04-17 03:10:46.308000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1152279008aa'
down_revision = '89ee48680e79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('public_sharing', sa.Boolean(), nullable=False))
    op.alter_column('questionnaire', 'post',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questionnaire', 'post',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.drop_column('application', 'public_sharing')
    # ### end Alembic commands ###
