# REST API with Django

This project explores building a REST API using Django.

## uv

We use 'uv' to manage dependencies, virtual environments and python versions.

[Installation instructions for 'uv' here](https://docs.astral.sh/uv/getting-started/installation/)

Set .python-version to your desired version, and 'uv' will handle it from there.

### 'uv' commands

Sync dependencies, venv and python all-in-one

    uv sync

Update all dependencies and store in lock file:

    uv lock --upgrade

## pre-commit

We use [pre-commit](https://pre-commit.com) to perform various code quality checks.

It was installed via `uv add pre-commit`.
We have already added the `default_install_hook_types: [pre-commit, pre-push, commit-msg]` line to the configuration file, so all you need to do to install the Git hooks, is to run:

    uv run pre-commit install

Run manually (without using the pre-commit hooks) on git-staged files:

    uv run pre-commit run

Run manually on all files, not just the staged ones:

    uv run pre-commit run --all-files

Periodically update hooks to their latest versions:

    uv run pre-commit autoupdate
