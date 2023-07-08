"""add foriegn key to post table

Revision ID: 8941e050c818
Revises: ed2d81344a50
Create Date: 2023-07-08 11:55:13.301967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8941e050c818'
down_revision = 'ed2d81344a50'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", 
                            local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
