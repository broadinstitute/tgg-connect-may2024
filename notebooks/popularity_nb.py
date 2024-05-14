from pathlib import Path

import hail as hl
import matplotlib.pyplot as plt

from tgg_movies.join_tables import join_movie_data
from tgg_movies.popularity_analysis import (
    calculate_movies_avg_rating,
    sort_movies_by_rating,
)

data_dir = Path("data/movies")

movies = hl.read_table(str(data_dir / "movies.ht"))
ratings = hl.read_table(str(data_dir / "ratings.ht"))
users = hl.read_table(str(data_dir / "users.ht"))

ht = join_movie_data(movies, ratings, users)
ht = calculate_movies_avg_rating(ht)
ht = sort_movies_by_rating(ht, n=1500)

ht_local = ht.collect()

avg_ratings = [row.avg_rating for row in ht_local]

# Save histogram as PNG
plt.hist(avg_ratings, bins=20, edgecolor="black")
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.title("Distribution of Movie Ratings")
plt.legend(["Movie Ratings"])
plt.savefig("movie_ratings_distribution.png")
plt.show()
