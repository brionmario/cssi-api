"""empty message

Revision ID: cb018c771a53
Revises: 
Create Date: 2019-04-16 01:05:44.197617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb018c771a53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('identifier', sa.String(length=100), nullable=False),
    sa.Column('developer', sa.String(length=100), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='fk_genre_id', use_alter=True),
    sa.ForeignKeyConstraint(['type_id'], ['application_type.id'], name='fk_type_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('application_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('display_name', sa.String(length=100), nullable=False),
    sa.Column('display_name_full', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('display_name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questionnaire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pre', sa.TEXT(), nullable=False),
    sa.Column('post', sa.TEXT(), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['session.id'], name='fk_session_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('expected_emotions', sa.TEXT(), nullable=False),
    sa.Column('cssi_score', sa.Float(), nullable=False),
    sa.Column('latency_scores', sa.TEXT(), nullable=False),
    sa.Column('total_latency_score', sa.Float(), nullable=False),
    sa.Column('sentiment_scores', sa.TEXT(), nullable=False),
    sa.Column('total_sentiment_score', sa.Float(), nullable=False),
    sa.Column('questionnaire_id', sa.Integer(), nullable=False),
    sa.Column('questionnaire_scores', sa.TEXT(), nullable=True),
    sa.Column('total_questionnaire_score', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['app_id'], ['application.id'], name='fk_app_id', use_alter=True),
    sa.ForeignKeyConstraint(['questionnaire_id'], ['questionnaire.id'], name='fk_questionnaire_id', use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    op.drop_table('questionnaire')
    op.drop_table('genre')
    op.drop_table('application_type')
    op.drop_table('application')
    # ### end Alembic commands ###
