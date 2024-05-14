import hail as hl


def test_join_movie_data(joint_table: hl.Table) -> None:
    # Expected fields after join
    expected_fields = {
        # "id",  # From movies_ht
        "title",  # From movies_ht
        "genres",  # From movies_ht
        "user_id",  # From ratings_ht
        "rating",  # From ratings_ht
        "age",  # From users_ht
        "sex",  # From users_ht
        "occupation",  # From users_ht
        "zipcode",  # From users_ht
    }

    # Extract fields from the resulting joined table
    result_fields = set(joint_table.row_value.keys())

    # Check if all expected fields exist in the result
    assert (
        expected_fields <= result_fields
    ), "Some expected fields are missing in the joined table."

    # Verify data from sample user to check the integrity of join
    sample_user_id = 196
    user_data = joint_table.filter(joint_table.user_id == sample_user_id).collect()

    # Assuming that user 196 has rated movie 1 with a rating of 5
    assert len(user_data) > 0, "No data found for sampled user."
    assert (
        user_data[0].title == "Toy Story (1995)"
    ), "Incorrect movie title for given user and movie."
    assert user_data[0].rating == 5, "Incorrect rating data."
    assert user_data[0].age == 25, "Incorrect user age."
    assert user_data[0].sex == "M", "Incorrect user sex."
    assert user_data[0].occupation == "technician", "Incorrect user occupation."
    assert user_data[0].zipcode == "02139", "Incorrect user zipcode."
