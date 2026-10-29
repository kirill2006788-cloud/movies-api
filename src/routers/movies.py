from typing import Literal

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import asc, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.models import Movie
from src.schemas import MovieCreate, MovieRead

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post("", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
async def create_movie(
    data: MovieCreate,
    session: AsyncSession = Depends(get_session),
):
    movie = Movie(**data.model_dump())
    session.add(movie)
    await session.commit()
    await session.refresh(movie)
    return movie


def build_movies_query(
    genre: str | None = None,
    year: int | None = None,
    min_rating: float | None = None,
    sort_by: Literal["title", "year", "rating"] = "title",
    order: Literal["asc", "desc"] = "asc",
):
    query = select(Movie)

    if genre:
        query = query.where(func.lower(Movie.genre) == genre.lower())
    if year is not None:
        query = query.where(Movie.year == year)
    if min_rating is not None:
        query = query.where(Movie.rating >= min_rating)

    sort_column = getattr(Movie, sort_by)
    sort_function = desc if order == "desc" else asc
    return query.order_by(sort_function(sort_column))


@router.get("", response_model=list[MovieRead])
async def get_movies(
    genre: str | None = None,
    year: int | None = Query(None, ge=1888),
    min_rating: float | None = Query(None, ge=0, le=10),
    sort_by: Literal["title", "year", "rating"] = "title",
    order: Literal["asc", "desc"] = "asc",
    session: AsyncSession = Depends(get_session),
):
    query = build_movies_query(genre, year, min_rating, sort_by, order)

    result = await session.scalars(query)
    return result.all()
