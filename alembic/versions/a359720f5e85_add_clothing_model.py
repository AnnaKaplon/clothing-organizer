"""add clothing model

Revision ID: a359720f5e85
Revises: bdb793c768c7
Create Date: 2020-02-08 12:50:30.099443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a359720f5e85'
down_revision = 'bdb793c768c7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "clothing",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("clothing_type", sa.Enum, nullable=False),
        sa.Column("color", sa.Enum, nullable=False),
        sa.Column("buy_date", sa.Date),
        sa.Column("picture_url", sa.String)
    )

    op.create_table(
        "wearing",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("clothing_id", sa.Integer, sa.ForeignKey("clothing.id"))
    )

    op.create_table(
        "washing",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("clothing_id", sa.Integer, sa.ForeignKey("clothing.id"))
    )


def downgrade():
    op.drop_table("washing")
    op.drop_table("wearing")
    op.drop_table("clothing")
