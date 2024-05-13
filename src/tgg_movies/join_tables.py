import hail as hl


def join_movie_data(
    movies_ht: hl.Table,
    ratings_ht: hl.Table,
    users_ht: hl.Table,
) -> hl.Table:
    """
    Join movies, ratings, and users Hail tables into one Hail table with all details.

    Parameters:
        movies_ht (hl.Table): Hail table containing movies data.
        ratings_ht (hl.Table): Hail table containing ratings data.
        users_ht (hl.Table): Hail table containing users data.

    Returns:
        hl.Table: A Hail table resulting from the join of movies,
        ratings, and users data.
    """
    # Join movies with ratings on movie_id
    movies_ratings_joined = movies_ht.key_by("id").join(
        ratings_ht.key_by("movie_id"),
        how="inner",
    )

    # Join the result with users on user_id
    return (
        movies_ratings_joined.key_by("user_id")
        .join(users_ht.key_by("id"), how="inner")
        .key_by("id")
    )
