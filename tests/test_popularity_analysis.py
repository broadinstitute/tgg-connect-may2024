import hail as hl
import pytest

from tgg_movies.popularity_analysis import (
    calculate_movies_avg_rating,
    sort_movies_by_rating,
)


@pytest.fixture(scope="module")
def joined_ht() -> hl.Table:
    """
    Pytest fixture to create a mock Hail Table using `hl.parallelize`
    that mimics the schema and data of the joined movies, ratings, and users dataset.

    Returns:
        A Hail Table object that simulates the joined dataset.
    """
    joined_data = [
        {
            "user_id": 1,
            "id": 1,
            "title": "Toy Story (1995)",
            "genres": ["Animation", "Children's", "Comedy"],
            "rating": 5,
            "age": 24,
            "sex": "M",
            "occupation": "technician",
            "zipcode": "85711",
        },
        {
            "user_id": 2,
            "id": 1,
            "title": "Toy Story (1995)",
            "genres": ["Animation", "Children's", "Comedy"],
            "rating": 4,
            "age": 53,
            "sex": "F",
            "occupation": "other",
            "zipcode": "94043",
        },
    ]
    joined_schema = """
    array<struct{
        user_id: int32,
        id: int32,
        title: str,
        genres: array<str>,
        rating: int32,
        age: int32,
        sex: str,
        occupation: str,
        zipcode: str
    }>"""
    ht_joined = hl.Table.parallelize(
        hl.literal(joined_data, joined_schema), key=["user_id", "id"]
    )

    ht_joined = hl.Table.parallelize(hl.literal(joined_data, joined_schema), key=["id"])
    return ht_joined


# calculate_movies_avg_rating()
def test_calculate_movies_avg_rating(joined_ht):
    # Generate the average ratings table
    avg_ratings = calculate_movies_avg_rating(joined_ht)

    avg_ratings.describe()
    avg_ratings.show()

    # Collect the results
    result = avg_ratings.collect()

    # Expected results
    expected_result = [
        hl.Struct(**{"id": 1, "title": "Toy Story (1995)", "avg_rating": 4.5})
    ]

    # Assert the results
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


# write tests for sort_movies_by_rating, creating a new mock hail table with 10 movies. The HT schema should resemble {"id": 1, "title": "Toy Story (1995)", "avg_rating": 4.5}
def create_mock_movies_ht():
    """
    Function to create a mock Hail Table for testing sorting by rating.

    Returns:
        A Hail Table with a schema resembling {"id": int32, "title": str, "avg_rating": float64}
    """
    mock_movies_data = [
        {"id": 1, "title": "Toy Story (1995)", "avg_rating": 4.5},
        {"id": 2, "title": "Jumanji (1995)", "avg_rating": 3.7},
        {"id": 3, "title": "Grumpier Old Men (1995)", "avg_rating": 3.2},
        {"id": 4, "title": "Waiting to Exhale (1995)", "avg_rating": 3.4},
        {"id": 5, "title": "Father of the Bride Part II (1995)", "avg_rating": 3.1},
        {"id": 6, "title": "Heat (1995)", "avg_rating": 4.1},
        {"id": 7, "title": "Sabrina (1995)", "avg_rating": 3.8},
        {"id": 8, "title": "Tom and Huck (1995)", "avg_rating": 2.9},
        {"id": 9, "title": "Sudden Death (1995)", "avg_rating": 3.5},
        {"id": 10, "title": "GoldenEye (1995)", "avg_rating": 4.3},
    ]
    schema = hl.tstruct(id=hl.tint32, title=hl.tstr, avg_rating=hl.tfloat64)
    ht = hl.Table.parallelize(
        [hl.Struct(**d) for d in mock_movies_data], schema=schema, key=["id"]
    )
    return ht


def test_sort_movies_by_rating():
    ht = create_mock_movies_ht()

    # Test sorting in descending order (top 10 movies)
    sorted_ht = sort_movies_by_rating(ht, top=True, n=3)
    sorted_top_result = sorted_ht.collect()
    expected_top_result = sorted(
        ht.collect(), key=lambda x: x.avg_rating, reverse=True
    )[:3]
    assert (
        sorted_top_result == expected_top_result
    ), f"Expected {expected_top_result}, but got {sorted_top_result}"

    # Test sorting in ascending order (bottom 10 movies)
    sorted_ht = sort_movies_by_rating(ht, top=False, n=3)
    sorted_bottom_result = sorted_ht.collect()
    expected_bottom_result = sorted(ht.collect(), key=lambda x: x.avg_rating)[:3]
    assert (
        sorted_bottom_result == expected_bottom_result
    ), f"Expected {expected_bottom_result}, but got {sorted_bottom_result}"
