"""initial migration

Revision ID: 615bcf03a452
Revises:
Create Date: 2024-03-20 11:50:48.112752

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "615bcf03a452"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "architecture",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "manufacturer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("website", sa.String(), nullable=False),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "cpu",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("manufacturer", sa.String(), nullable=False),
        sa.Column("architecture_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["architecture_id"],
            ["architecture.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "operatingsystem",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("version", sa.String(), nullable=False),
        sa.Column("architecture_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["architecture_id"],
            ["architecture.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "computer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("computer_type", sa.String(), nullable=False),
        sa.Column("purchase_date", sa.Date(), nullable=True),
        sa.Column("original_cost", sa.Float(), nullable=True),
        sa.Column("installed_memory", sa.Integer(), nullable=True),
        sa.Column("max_memory", sa.Integer(), nullable=True),
        sa.Column("system_model", sa.String(), nullable=True),
        sa.Column("serial_number", sa.String(), nullable=True),
        sa.Column("soft_deleted", sa.Boolean(), nullable=False),
        sa.Column("manufacturer_id", sa.Integer(), nullable=True),
        sa.Column("operating_system_id", sa.Integer(), nullable=True),
        sa.Column("cpu_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["cpu_id"],
            ["cpu.id"],
        ),
        sa.ForeignKeyConstraint(
            ["manufacturer_id"],
            ["manufacturer.id"],
        ),
        sa.ForeignKeyConstraint(
            ["operating_system_id"],
            ["operatingsystem.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("computer")
    op.drop_table("operatingsystem")
    op.drop_table("cpu")
    op.drop_table("manufacturer")
    op.drop_table("architecture")
    # ### end Alembic commands ###
