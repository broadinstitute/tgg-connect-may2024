import hail as hl
import pytest

from tgg_movies.join_tables import join_movie_data


@pytest.fixture(scope="module")
def movies_ht() -> hl.Table:
    """
    Pytest fixture to create a mock Hail Table using `hl.parallelize`
    that mimics the schema of the movies.ht dataset.

    Returns:
        A Hail Table object that simulates the movies dataset.
    """
    movies_data = [
        {
            "id": 1,
            "title": "Toy Story (1995)",
            "genres": ["Animation", "Children's", "Comedy"],
        },
        {
            "id": 2,
            "title": "GoldenEye (1995)",
            "genres": ["Action", "Adventure", "Thriller"],
        },
        {"id": 3, "title": "Four Rooms (1995)", "genres": ["Thriller"]},
        {
            "id": 4,
            "title": "Get Shorty (1995)",
            "genres": ["Action", "Comedy", "Drama"],
        },
        {"id": 5, "title": "Copycat (1995)", "genres": ["Crime", "Drama", "Thriller"]},
        {
            "id": 6,
            "title": "Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)",
            "genres": ["Drama"],
        },
        {"id": 7, "title": "Twelve Monkeys (1995)", "genres": ["Drama", "Sci-Fi"]},
        {"id": 8, "title": "Babe (1995)", "genres": ["Children's", "Comedy", "Drama"]},
        {"id": 9, "title": "Dead Man Walking (1995)", "genres": ["Drama"]},
        {"id": 10, "title": "Richard III (1995)", "genres": ["Drama", "War"]},
    ]
    movies_schema = "array<struct{id: int32, title: str, genres: array<str>}>"
    ht_movies = hl.Table.parallelize(hl.literal(movies_data, movies_schema), key=["id"])
    return ht_movies


@pytest.mark.parametrize("field", ["id", "title", "genres"])
def test_movie_fields_exist(movies_ht: hl.Table, field: str) -> None:
    """
    Test to verify that each specified field exists in every row of the Hail table.
    """
    fields = list(movies_ht.row)

    assert field in fields, f"{field} field is missing"


@pytest.fixture(scope="module")
def ratings_ht() -> hl.Table:
    """
    Pytest fixture to create a mock Hail Table using `hl.parallelize`
    that mimics the schema of the ratings.ht dataset and matches the IDs
    from the movies.ht dataset for consistent data testing.

    Returns:
        A Hail Table object that simulates the ratings dataset.
    """
    ratings_data = [
        {"user_id": 196, "movie_id": 1, "rating": 5},
        {"user_id": 186, "movie_id": 2, "rating": 3},
        {"user_id": 22, "movie_id": 1, "rating": 3},
        {"user_id": 244, "movie_id": 2, "rating": 4},
        {"user_id": 166, "movie_id": 3, "rating": 1},
        {"user_id": 298, "movie_id": 4, "rating": 4},
        {"user_id": 115, "movie_id": 3, "rating": 2},
        {"user_id": 253, "movie_id": 5, "rating": 5},
        {"user_id": 305, "movie_id": 5, "rating": 5},
        {"user_id": 6, "movie_id": 1, "rating": 4},
    ]
    ratings_schema = "array<struct{user_id: int32, movie_id: int32, rating: int32}>"
    ht_ratings = hl.Table.parallelize(
        hl.literal(ratings_data, ratings_schema),
        key=["user_id", "movie_id"],
    )
    return ht_ratings


@pytest.fixture(scope="module")
def users_ht() -> hl.Table:
    """
    Pytest fixture to create a mock Hail Table using `hl.parallelize`
    that mimics the schema of the users.ht dataset and matches the user IDs
    from the ratings.ht dataset for consistent data testing.

    Returns:
        A Hail Table object that simulates the users dataset.
    """
    users_data = [
        {
            "id": 196,
            "age": 25,
            "sex": "M",
            "occupation": "technician",
            "zipcode": "02139",
        },
        {
            "id": 186,
            "age": 33,
            "sex": "F",
            "occupation": "executive",
            "zipcode": "11238",
        },
        {"id": 22, "age": 59, "sex": "M", "occupation": "writer", "zipcode": "90210"},
        {
            "id": 244,
            "age": 28,
            "sex": "M",
            "occupation": "engineer",
            "zipcode": "10016",
        },
        {
            "id": 166,
            "age": 47,
            "sex": "M",
            "occupation": "administrator",
            "zipcode": "55105",
        },
        {"id": 298, "age": 44, "sex": "M", "occupation": "lawyer", "zipcode": "20006"},
        {"id": 115, "age": 26, "sex": "F", "occupation": "artist", "zipcode": "30301"},
        {
            "id": 253,
            "age": 30,
            "sex": "F",
            "occupation": "librarian",
            "zipcode": "22903",
        },
        {"id": 305, "age": 23, "sex": "M", "occupation": "student", "zipcode": "94043"},
        {"id": 6, "age": 42, "sex": "M", "occupation": "executive", "zipcode": "98101"},
    ]
    users_schema = (
        "array<struct{id: int32, age: int32, sex: str, occupation: str, zipcode: str}>"
    )
    ht_users = hl.Table.parallelize(hl.literal(users_data, users_schema), key=["id"])
    return ht_users


@pytest.fixture(scope="module")
def joint_table(
    movies_ht: hl.Table, ratings_ht: hl.Table, users_ht: hl.Table
) -> hl.Table:
    return join_movie_data(movies_ht, ratings_ht, users_ht)
