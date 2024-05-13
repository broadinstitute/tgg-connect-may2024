import hail as hl
from pathlib import Path

from tgg_movies.join_tables import join_movie_data


data_dir = Path("data/movies")

movies = hl.read_table(str(data_dir / "movies.ht"))
ratings = hl.read_table(str(data_dir / "ratings.ht"))
users = hl.read_table(str(data_dir / "users.ht"))

ht = join_movie_data(movies, ratings, users)
