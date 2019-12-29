"""add active column to user model

Revision ID: bdb793c768c7
Revises: 758c815c7f4b
Create Date: 2019-12-25 13:51:15.708126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdb793c768c7'
down_revision = '758c815c7f4b'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()

    op.add_column('user', sa.Column('active', sa.Boolean))
    connection.execute(sa.text('UPDATE "user" SET active = TRUE WHERE active IS NULL;'))
    op.alter_column('user', 'active', nullable=False)


def downgrade():
    op.drop_column('user', 'active')
