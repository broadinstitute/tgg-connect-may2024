# tgg-movies

## Detailed Usage

### 1. Install tox using pipx

Tox is a tool for automating testing and development tasks in isolated
environments. You can use pipx, a package runner for Python applications, to
install tox. The command is simply:

```bash
pipx install tox
```

### 3. Create and Activate a Virtual Environment

Virtual environments in Python isolate project dependencies, ensuring different
projects don't interfere with each other. To create and activate a new virtual
environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Install the Dependencies

The requirements.txt file lists the Python dependencies for your project. Using
pip-tools, we can pin the exact version of each dependency to ensure
reproducible builds.

Install the core python dependencies then install the project dependencies using
pip-tools:

```bash
python -m pip install --upgrade pip setuptools wheel pip-tools
pip-sync
```

You can optionally use pip-tools to update all dependencies before running
`pip-sync`. This isn't strictly necessary as I keep this repository more-or-less
up to date, and dependabot will submit pull requests for out of date packages
automatically.

```bash
pip-compile --all-extras --resolver=backtracking --upgrade pyproject.toml
```

Note: You can always reference the command to pin dependencies in a comment at
the top of requirements.txt.

### 5. Install the First-Party Package in Editable Mode

The -e option allows pip to install the package in editable mode. This means
changes to the source code will immediately affect the package without needing
to reinstall it:

```bash
python -m pip install -e .
```

### 6. Install the Pre-commit Hooks

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

### 7. Run the Test Suite with tox

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

### 8. Replace the Project Name

Now replace the placeholder project name tgg_movies/tgg-movies
with the name of your actual project throughout the project files.

### 9. Update Project Metadata

Update the project metadata in both pyproject.toml and README.md to match your
project's details.

### 10. Write Code and Lint it

Now write your code! After that, you can run linting checks and auto-fix issues
using tox:

```bash
tox -e fix
```

Take a look at `tox.ini` for a reference on using the various tools directly
from the command line. During development, you don't always need to execute
through tox's isolated environments.
