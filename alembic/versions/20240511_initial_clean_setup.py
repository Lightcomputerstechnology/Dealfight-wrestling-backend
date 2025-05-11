"""initial clean setup

Revision ID: 20240511_initial
Revises: 
Create Date: 2025-05-11 12:00:00

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg

# revision identifiers, used by Alembic.
revision = '20240511_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('username', sa.String(), nullable=False, unique=True, index=True),
        sa.Column('email', sa.String(), nullable=False, unique=True, index=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_admin', sa.Integer(), default=0),
        sa.Column('coins', sa.Integer(), default=0),
        sa.Column('diamonds', sa.Integer(), default=0),
        sa.Column('xp', sa.Integer(), default=0),
        sa.Column('level', sa.Integer(), default=1),
        sa.Column('matches_played', sa.Integer(), default=0),
        sa.Column('matches_won', sa.Integer(), default=0),
    )

    op.create_table('xp_logs',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('xp_gained', sa.Integer(), nullable=False),
        sa.Column('level', sa.Integer(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
    )

    op.create_table('wallets',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), unique=True),
        sa.Column('coins', sa.Integer(), default=0),
        sa.Column('diamonds', sa.Integer(), default=0),
    )

    op.create_table('wrestlers',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('gender', sa.String(), nullable=False),
        sa.Column('strength', sa.Integer(), default=50),
        sa.Column('agility', sa.Integer(), default=50),
        sa.Column('charisma', sa.Integer(), default=50),
        sa.Column('owner_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE')),
    )

    op.create_table('title_belts',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('type', sa.Enum('World', 'Tag Team', 'Women', name='titletype'), nullable=False),
        sa.Column('holder_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )

    op.create_table('support_tickets',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('subject', sa.String(), nullable=False),
        sa.Column('message', sa.String(), nullable=False),
        sa.Column('status', sa.String(), default='open'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table('reports',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('reporter_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('reported_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('reason', sa.String(), nullable=False),
        sa.Column('details', sa.String(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
    )

    op.create_table('replays',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('match_id', sa.Integer(), index=True),
        sa.Column('player_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('events', pg.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table('referrals',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('referred_email', sa.String(), nullable=False),
        sa.Column('reward_claimed', sa.Integer(), default=0),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

    op.create_table('notifications',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('message', sa.String(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
    )

    op.create_table('matches',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('type', sa.Enum('single', 'tag', name='matchtype'), default='single'),
        sa.Column('status', sa.String(), default='pending'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('player1_id', sa.Integer(), sa.ForeignKey('users.id')),
        sa.Column('player2_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=True),
    )

def downgrade():
    op.drop_table('matches')
    op.drop_table('notifications')
    op.drop_table('referrals')
    op.drop_table('replays')
    op.drop_table('reports')
    op.drop_table('support_tickets')
    op.drop_table('title_belts')
    op.drop_table('wrestlers')
    op.drop_table('wallets')
    op.drop_table('xp_logs')
    op.drop_table('users')
    op.execute('DROP TYPE IF EXISTS titletype')
    op.execute('DROP TYPE IF EXISTS matchtype')