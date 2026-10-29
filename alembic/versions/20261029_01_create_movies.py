"""create movies table

Revision ID: 20261029_01
Revises:
"""

from alembic import op
import sqlalchemy as sa


revision = "20261029_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "movies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("genre", sa.String(), nullable=False),
        sa.Column("rating", sa.Float(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "rating >= 0 AND rating <= 10",
            name="check_movie_rating_range",
        ),
        sa.CheckConstraint("year >= 1888", name="check_movie_year_1888"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_movies_id"), "movies", ["id"])
    op.create_index(op.f("ix_movies_title"), "movies", ["title"])


def downgrade() -> None:
    op.drop_index(op.f("ix_movies_title"), table_name="movies")
    op.drop_index(op.f("ix_movies_id"), table_name="movies")
    op.drop_table("movies")
