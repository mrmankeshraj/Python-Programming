"""Create Post Table

Revision ID: 929695f60a0c
Revises: 
Create Date: 2023-07-08 11:23:27.846718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '929695f60a0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    

def downgrade():
    op.drop_table("posts")
    
