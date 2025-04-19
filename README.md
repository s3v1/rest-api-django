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

## pre-commit

We use [pre-commit}(https://pre-commit.com) to check several quality related things.

It's already added, but if you want to know how here is how the install was done: "uv add pre-commit"
and then we added the "default_install_hook_types: [pre-commit, pre-push, commit-msg]" line in the config file, we just need to do this ONE TIME to let pre-commit install the git hooks:

    uv run pre-commit install

Run manually (without using the pre-commit hooks) on git-staged files:

    uv run pre-commit run

Run manually on all files, not just the staged ones:

    uv run pre-commit run --all-files

Update all the hooks to latest tags once in a while:

    uv run pre-commit autoupdate
