# REST API with Django

This project is exploring making a REST API based on Django

## uv

We use 'uv' to manage dependencies, virtual environments and python versions.

[Installation instructions for 'uv' here](https://docs.astral.sh/uv/getting-started/installation/)

Set .python-version to you desired version and 'uv' will handle it from there.

### 'uv' commands

Sync dependencies, venv and python all-in-one

    uv sync

Update all dependencies and store in lock file:

    uv lock --upgrade
