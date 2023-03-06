"""empty message

Revision ID: 785b5da40e00
Revises: 9eefca109345
Create Date: 2023-03-06 16:17:12.716484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "785b5da40e00"
down_revision = "9eefca109345"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("cats", sa.Column("foo", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("cats", "foo")
    # ### end Alembic commands ###