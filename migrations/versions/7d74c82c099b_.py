"""empty message

Revision ID: 7d74c82c099b
Revises: 57d5ac310a9f
Create Date: 2023-03-10 19:24:34.960157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d74c82c099b'
down_revision = '57d5ac310a9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_repeat', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_repeat')
    # ### end Alembic commands ###