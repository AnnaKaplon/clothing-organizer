"""make user email unique

Revision ID: 758c815c7f4b
Revises: 27a8e86a1265
Create Date: 2019-12-22 14:41:16.485612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '758c815c7f4b'
down_revision = '27a8e86a1265'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint('user_email', 'user', ['email'])


def downgrade():
    op.drop_constraint('user_email', 'user')
