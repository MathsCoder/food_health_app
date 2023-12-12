"""empty message

Revision ID: 3c84a39df2ab
Revises: 
Create Date: 2023-12-04 16:36:45.771269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3c84a39df2ab"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(length=200), nullable=False),
        sa.Column("registration_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "image",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("file_path", sa.String(length=255), nullable=False),
        sa.Column("uploaded_time", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("image")
    op.drop_table("user")
    # ### end Alembic commands ###
