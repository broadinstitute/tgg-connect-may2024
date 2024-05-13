# TGG Connect DayCoding Group Breakout

_May 14, 2024_

## Goal: LLM-driven development with Hail

### Guidelines:

Collaboratively explore test-driven development using large language model (LLM) coding tools!

One team member will operate the coding tools, while others will contribute prompts. Aim to minimize manual coding to push the boundaries of these tools.

Remember, AI coding tools often make mistakes! Writing tests is crucial. Executing `tox` will assess your test coverage.

Since so many of us work with Hail, we utilize the "movie lens" dataset that Hail can download for us. This includes 1,682 movies, 100,000 movie reviews from 943 users. See `schemas.txt` for what the data looks like. use the `get_movies_data.py` script to download it.

Write library functions in the `src` , tests in `tests`, and exploratory work in the `notebooks` dirs.

Below are several project ideas for your group. There is no single correct approach—enjoy experimenting in your team.

## Development ideas

1. **Movie Popularity Analysis**

   - **Objective:** Determine the popularity of movies by analyzing rating distributions.
   - **Task:** Calculate each movie's average rating, list the top and bottom 10 by rating, and visualize the results.

2. **User Engagement Study**

   - **Objective:** Identify which user demographics are most active in rating movies.
   - **Task:** Aggregate and visualize ratings by age, sex, and occupation.

3. **Genre Preferences by Demographics**

   - **Objective:** Investigate how movie genre preferences vary among different demographics.
   - **Task:** Analyze the most popular genres within user segments defined by age and sex.

4. **Collaborative Filtering From Scratch**

   - **Objective:** Develop a basic collaborative filtering algorithm for movie recommendations.
   - **Task:** Construct a user-item rating matrix to identify similar users and recommend movies.

5. **Temporal Trends in Movie Ratings**

   - **Objective:** Explore how movie ratings have evolved over time.
   - **Task:** Plot average movie ratings over different release years or periods.

6. **Sentiment Analysis of Movie Titles**

   - **Objective:** Examine the relationship between the sentiment of movie titles and their ratings.
   - **Task:** Apply sentiment analysis to movie titles and correlate the results with average ratings.

7. **Geographic Analysis of User Activity**

   - **Objective:** Analyze geographic patterns in user activity or preferences.
   - **Task:** Map user activity or preferences by zip code.

8. **Impact of Movie Genres on Ratings**

   - **Objective:** Evaluate whether certain genres consistently receive higher or lower ratings.
   - **Task:** Calculate average ratings per genre and compare them using bar charts.

9. **Advanced Filtering Interface**

   - **Objective:** Create a dynamic filtering interface for querying the dataset.
   - **Task:** Build a search interface in Hail that supports multiple criteria such as genre, demographics, and rating thresholds.

10. **Movie Recommendation System**
    - **Objective:** Construct a simple movie recommendation system.
    - **Task:** Develop user profiles based on past ratings, match these to genre preferences, and suggest new movies.

## Installation

### 1. Create and Activate a Virtual Environment

Virtual environments in Python isolate project dependencies, ensuring different
projects don't interfere with each other. To create and activate a new virtual
environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install the Dependencies

The requirements.txt file lists the Python dependencies for your project. Using
pip-tools, we can pin the exact version of each dependency to ensure
reproducible builds.

Install the core python dependencies then install the project dependencies using
pip-tools:

```bash
python -m pip install --upgrade pip setuptools wheel pip-tools
pip-sync
```

### 3. Install the First-Party Package in Editable Mode

The -e option allows pip to install the package in editable mode. This means
changes to the source code will immediately affect the package without needing
to reinstall it:

```bash
python -m pip install -e .
```

### 4. Install the Pre-commit Hooks

Pre-commit is a framework for managing git pre-commit hooks. These checks are
run before your changes are committed to ensure code quality. To install
pre-commit hooks:

```bash
pre-commit install
```

You can also update the hook versions:

```bash
pre-commit autoupdate
```

### 5. Run the Test Suite with tox

Now you can run the project's test suite using the previously installed tox
tool:

```bash
tox
```

By default, this will create environments for py310, py311 and py312. This
assumes all versions of python are available on your system. Take a look at
pyenv to make this easy.

You can add additional python versions to test against by modifying `tox.ini`
and the corresponding github-action workflow.

### 6. Write Code and Lint it

Now write your code! After that, you can run linting checks and auto-fix issues
using tox:

```bash
tox -e fix
```

Take a look at `tox.ini` for a reference on using the various tools directly
from the command line. During development, you don't always need to execute
through tox's isolated environments.

### 7. Add New Dependencies

When you need to add new dependencies to the project, update the `pyproject.toml` configuration to include the new packages. After adding the dependencies, generate a new `requirements.txt` file to reflect these changes and ensure compatibility across environments:

```bash
pip-compile --all-extras --resolver=backtracking pyproject.toml
```

Then, synchronize the project's virtual environment to install newly added dependencies:

```bash
pip-sync
```

Remember to commit both the updated `pyproject.toml` and `requirements.txt` files to version control. This ensures other contributors and environments like CI/CD systems use the same dependencies.
