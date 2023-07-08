"""add last few columns to posts table

Revision ID: 70f1b8e1f6e1
Revises: 8941e050c818
Create Date: 2023-07-08 12:02:35.646206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70f1b8e1f6e1'
down_revision = '8941e050c818'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at",
                                    sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
