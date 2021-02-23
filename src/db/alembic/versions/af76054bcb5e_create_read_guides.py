"""create read_guides

Revision ID: af76054bcb5e
Revises: e9b37b524d49
Create Date: 2020-12-01 08:56:56.143515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af76054bcb5e'
down_revision = 'e9b37b524d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('read_guides',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('channel_id', sa.String(), nullable=False),
                    sa.Column('user_id', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('read_guides')