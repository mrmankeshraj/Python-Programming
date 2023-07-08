"""add users table

Revision ID: ed2d81344a50
Revises: cfc637b6f5dd
Create Date: 2023-07-08 11:45:15.745466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed2d81344a50'
down_revision = 'cfc637b6f5dd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("Created_at", sa.TIMESTAMP(timezone=True),
                            server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )


def downgrade():
    op.drop_table("users")
