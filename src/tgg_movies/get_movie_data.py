"""Module for handling movie data operations using Hail."""

from pathlib import Path

import hail as hl
from loguru import logger

if __name__ == "__main__":
    if not Path("data/movies").exists():
        logger.info("Loading movie lens data...")
        hl.utils.get_movie_lens("data/movies")
    else:
        logger.info("Movie lens data already exists. Skipping download.")

    logger.info("Reading movies data...")
    movies = hl.read_table("data/movies.ht")
    logger.info("Describing movies data...")
    movies.describe()
    logger.info("Showing movies data...")
    movies.show()

    logger.info("Reading ratings data...")
    ratings = hl.read_table("data/ratings.ht")
    logger.info("Describing ratings data...")
    ratings.describe()
    logger.info("Showing ratings data...")
    ratings.show()

    logger.info("Reading users data...")
    users = hl.read_table("data/users.ht")
    logger.info("Describing users data...")
    users.describe()
    logger.info("Showing users data...")
    users.show()
