"""sqlite_init

Revision ID: sqlite_init
Revises: 
Create Date: 2025-07-01 11:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import sqlite
import uuid


# revision identifiers, used by Alembic.
revision = 'sqlite_init'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create user table
    op.create_table(
        'user',
        sa.Column('id', sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
        sa.Column('email', sa.String(255), nullable=False, unique=True, index=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('is_superuser', sa.Boolean(), nullable=False, default=False),
        sa.Column('full_name', sa.String(255), nullable=True),
    )

    # Create item table
    op.create_table(
        'item',
        sa.Column('id', sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('owner_id', sa.String(36), sa.ForeignKey('user.id', ondelete='CASCADE'), nullable=False),
    )


def downgrade():
    op.drop_table('item')
    op.drop_table('user')
