# Intro

This is a log of almost all the steps taken in this repo.

## Log

It's a python project so we start with uv
Install from here: [Astral UV Installation](https://docs.astral.sh/uv/getting-started/installation/)

Then:

    uv init
    uv add pre-commit --dev

Updated description in pyproject.toml

    uv run hello.py
    uv run pre-commit sample-config >.pre-commit-config.yaml
    uv run pre-commit install

got tired of uv run all the time:

    . .venv/bin/activate

Run pre-commit hooks manually:

    pre-commit run --all-files

Added this to the precommit yaml config file

    -   id: markdownlint/markdownlint

Then again:

    pre-commit run --all-files

Which fails and tells me to

    pre-commit autoupdate

Adding more hooks from <https://pre-commit.com/hooks.html>

Added [typos documentation](https://github.com/crate-ci/typos/blob/master/docs/pre-commit.md)

Added [codespell documentation](https://github.com/codespell-project/codespell?tab=readme-ov-file#pre-commit-hook)

Added [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli)

Added [Pymarkdown](https://github.com/jackdewinter/pymarkdown)

Updated .python-version to 3.12.7
