"""Module for handling movie data operations using Hail."""

import sys
from pathlib import Path

import hail as hl
from loguru import logger

home_dir = str(Path.home())
data_dir = Path("data/movies")

logger.remove()
logger.add(sys.stdout, format="{time} {level} {message} {file}")

if __name__ == "__main__":
    if not data_dir.exists():
        logger.info(f"Loading movie lens data into {data_dir}...")
        hl.utils.get_movie_lens(str(data_dir))
    else:
        logger.info("Movie lens data already exists. Skipping download.")

    logger.info(f"Reading movies data from {data_dir}/movies.ht...")
    movies = hl.read_table(str(data_dir / "movies.ht"))
    logger.info("Describing movies data...")
    movies.describe()
    logger.info("Showing movies data...")
    movies.show()

    logger.info(f"Reading ratings data from {data_dir}/ratings.ht...")
    ratings = hl.read_table(str(data_dir / "ratings.ht"))
    logger.info("Describing ratings data...")
    ratings.describe()
    logger.info("Showing ratings data...")
    ratings.show()

    logger.info(f"Reading users data from {data_dir}/users.ht...")
    users = hl.read_table(str(data_dir / "users.ht"))
    logger.info("Describing users data...")
    users.describe()
    logger.info("Showing users data...")
    users.show()
