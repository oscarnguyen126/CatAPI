"""empty message

Revision ID: f7c4d5bf207c
Revises: ac6c8e48e0e4
Create Date: 2023-03-09 00:32:12.790485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f7c4d5bf207c"
down_revision = "ac6c8e48e0e4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dogs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("breed", sa.String(), nullable=True),
        sa.Column("origin", sa.String(), nullable=True),
        sa.Column("color", sa.String(), nullable=True),
        sa.Column("height", sa.String(), nullable=True),
        sa.Column("eyes_color", sa.String(), nullable=True),
        sa.Column("longevity", sa.Date(), nullable=True),
        sa.Column("character", sa.String(), nullable=True),
        sa.Column("health_problems", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_dogs_id"), "dogs", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_dogs_id"), table_name="dogs")
    op.drop_table("dogs")
    # ### end Alembic commands ###
