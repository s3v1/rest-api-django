# REST API with Django

This project is exploring making a REST API based on Django

## pre-commit

We use pre-commit to check several quality related things.

[Install pre-commit instructions}(https://pre-commit.com/index.html#install),
but here's the short version:

    uv add pre-commit

because we already set the "default_install_hook_types: [pre-commit, pre-push, commit-msg]" line in the config file, we just need to do this to let pre-commit install the git hooks:

    uv run pre-commit install

Run manually on git-staged files:

    uv run pre-commit run

Run manually on all files, not just the staged ones:

    uv run pre-commit run --all-files

Update all the hooks to latest tags:

    uv run pre-commit autoupdate

## uv

We use 'uv' to manage dependencies, virtual environments and python versions.

[Installation instructions for 'uv' here](https://docs.astral.sh/uv/getting-started/installation/)

Set .python-version to you desired version and 'uv' will handle it from there.

### 'uv' commands

Sync dependencies, venv and python all-in-one

    uv sync

Update all dependencies and store in lock file:

    uv lock --upgrade
