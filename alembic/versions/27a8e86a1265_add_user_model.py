"""add user model

Revision ID: 27a8e86a1265
Revises: 
Create Date: 2019-12-07 16:22:11.016728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27a8e86a1265'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False)

    )


def downgrade():
    op.drop_table('user')
