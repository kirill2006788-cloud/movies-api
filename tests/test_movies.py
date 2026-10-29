from src.routers.movies import build_movies_query


def test_movies_filters_and_sorting():
    query = build_movies_query(
        genre="drama",
        year=1994,
        min_rating=8,
        sort_by="rating",
        order="desc",
    )
    sql = str(query.compile(compile_kwargs={"literal_binds": True}))

    assert "lower(movies.genre)" in sql
    assert "movies.year = 1994" in sql
    assert "movies.rating >= 8" in sql
    assert "ORDER BY movies.rating DESC" in sql
