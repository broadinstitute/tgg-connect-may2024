# TGG Connect Day: Coding Group Breakout

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

If this doesn't work you may have another approach to creating venvs that are specific to your system (pyenv, conda).

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

## LLMs for software development

### What are LLMs and how do they work?

- Watch this: [Andrej Karpathy: Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)

### How are LLMs relevant to us as computational personnel?

- Automating code generation and completion
- Enhancing debugging and error detection
- Improving documentation
- Facilitating code review processes
- Assisting in learning new programming languages and frameworks
- **Reduce tedium so that we can focus on the real problem at hand**

### Don't get left behind

Even if you dislike using them now, LLMs will continue to improve. Keep up-to-date!

OpenAI's [ChatGPT-4o](https://openai.com/index/hello-gpt-4o) released yesterday

"**...new flagship model that can reason across audio, vision, and text in real time.**"

### Considerations for effective LLM use in software development

- How is LLM assistance executed in your environment?
- Are you pasting into a browser or are you using an editor integration?
- What information does it have access to (context window)?
- What model have you chosen (proprietary, open, fine-tuned)?
- How have you prompted it?
- What is the cost (flat rate vs. API)?
- How are you ensuring it is correct?
- How are you protecting sensitive info?

### Types of LLM assistance for software development

- Chat-based (e.g. ChatGPT web UI)
- Autocomplete (e.g. GitHub Copilot [VSCode extension](https://code.visualstudio.com/docs/copilot/overview))
- Inline chat writing/rewriting sections of code (e.g. [Neovim's gp.nvim](https://github.com/Robitx/gp.nvim))
- Changes across an entire code repository (e.g. [Copilot Workspaces](https://github.blog/2024-04-29-github-copilot-workspace/), [Cody](https://sourcegraph.com/cody), Devon)
- Systems-wide/infrastructure changes (to my knowledge, doesn't exist yet)

### The "context window" is very important to quality of results

What does the LLM know about your code?

- A single prompt?
- Your whole source tree?
- Consider the price of the context window!
- Remove wrong/unnecessary information from the context window
- Maximize type annotations in your code
- Add errors to the context to improve debugging

### Prompts

Providing consistent prompts...

- Ensures consistent code style, formatting, and methodologies
- Balance LLM output for concise vs. detailed responses
- Think of it like automation (run this prompt for everything I ask the LLM)

#### Prompts (example 1)

"You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so. Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question.

Our users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that. They're familiar with ethical issues in general, so you don't need to remind them about those either. Don't be verbose in your answers, but do provide details and examples where it might help the explanation."

From [Jeremy Howard: A Hackers' Guide to Language Models (YouTube)](https://www.youtube.com/watch?v=jkrNMKz9pWU)

### Example 2: Matt's python prompt

- Write all tests with pytest. Use pytest-mock where it is relevant
- When adding log statements, you will be using a preconfigured instance of loguru (from loguru import logger)
- Add conventional python docstrings for automated documentation generation. Try to be brief. Don't need to add docstrings to tests
- Use typical python exceptions where appropriate
- Using typing library where possible
- When defining classes, use @attr.define where necessary
- Return data objects as pydantic objects instead of dictionaries, defining the class if it does not exist
- Satisfy pyright type checker
- Line length, including docstrings, should be 88 characters including tabs. Break everything onto multiple lines, err toward line length ~70 if necessary

### Pricing

Flat rates: ~$20 to $30 for ChatGPT4/Copilot

[OpenAI API pricing](https://openai.com/api/pricing/)

e.g. so if my source tree has 30,000 tokens and I send the whole thing, it is $0.30.

### Ensuring correctness

- LLM code can be horrible; use tests!
- Iteration is key
- Give previous examples in the context
- Include expected inputs/outputs in the context

### Be careful

- Follow Broad LLM's [best practices](https://intranet.broadinstitute.org/gaiwg/best-practices-using-generative-ai-tools-work?check_logged_in=1)
- Always question results
- Avoid committing too much garbage AI-generated code (especially if you don't understand) 😂
- Very tempting to continuously have AI do the work
- _"The best LLM coding extension is your brain"_ -- Reddit User
