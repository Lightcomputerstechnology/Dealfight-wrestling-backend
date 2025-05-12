"""initial

Revision ID: 20240511_0001
Revises: 
Create Date: 2024-05-11 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20240511_0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(), nullable=False, unique=True),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_admin', sa.Integer(), default=0),
        sa.Column('coins', sa.Integer(), default=0),
        sa.Column('diamonds', sa.Integer(), default=0),
        sa.Column('xp', sa.Integer(), default=0),
        sa.Column('level', sa.Integer(), default=1),
        sa.Column('matches_played', sa.Integer(), default=0),
        sa.Column('matches_won', sa.Integer(), default=0)
    )

    op.create_table('faqs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('question', sa.String(), nullable=False),
        sa.Column('answer', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('is_active', sa.Boolean(), default=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False)
    )

    op.create_table('xp_logs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('xp_gained', sa.Integer(), nullable=False),
        sa.Column('level', sa.Integer(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False)
    )

def downgrade():
    op.drop_table('xp_logs')
    op.drop_table('faqs')
    op.drop_table('users')