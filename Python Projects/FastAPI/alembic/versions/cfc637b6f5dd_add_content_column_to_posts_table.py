"""add content column to posts table

Revision ID: cfc637b6f5dd
Revises: 929695f60a0c
Create Date: 2023-07-08 11:39:37.371745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfc637b6f5dd'
down_revision = '929695f60a0c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
    
