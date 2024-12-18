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

    uv sync

Added check-json to precommit

Added <https://github.com/pre-commit/sync-pre-commit-deps> to precommit

Added this precommit service/app to github, runs precommit for me: <https://pre-commit.ci/>

Updated .python-version to 3.13

Added action lint to precommit <https://github.com/rhysd/actionlint/blob/main/docs/usage.md#pre-commit>

Added commitizen to pre-commit <https://github.com/commitizen-tools/commitizen>
and <https://commitizen-tools.github.io/commitizen/getting_started/#integration-with-pre-commit>

Had a git push problem with commitizen:
"fatal: ambiguous argument 'origin/HEAD..HEAD': unknown revision or path not in the working tree."
Ran this to fix it:
<https://github.com/commitizen-tools/commitizen/issues/593#issuecomment-1865930350>:

    git remote set-head origin -a

Configured pymarkdown in pyproject.toml to allow longer lines (MD013)

Added gitlint <https://github.com/jorisroovers/gitlint>, to pre-commit. install instructions here: <https://jorisroovers.com/gitlint/latest/commit_hooks/#pre-commit>
Removed gitlint again. very annoying rules

Added a few more pre-commit hooks from: <https://medium.com/marvelous-mlops/welcome-to-pre-commit-heaven-5b622bb8ebce>

Added PyCQA/bandit too: <https://github.com/PyCQA/bandit>

Added     -   id: mixed-line-ending too

Added precommit for ruff: <https://github.com/astral-sh/ruff-pre-commit>
Added shellcheck precommit <https://github.com/shellcheck-py/shellcheck-py>

Add shellcheck pre-commit <https://pre-commit.com/#filtering-files-with-types> and added filtering with types to get executables. Otherwise it will look for  *s.sh files only <https://pre-commit.com/#filtering-files-with-types>

Added precommit hook for bashate <https://github.com/openstack/bashate>

Added precommit hook for pyupgrade <https://github.com/asottile/pyupgrade>

added debug-statements

added my py

added pytest and pytest-cov

made pytest work
upgrade coverage and set limit of 80%
configured bandit to ignore tests folder <https://bandit.readthedocs.io/en/latest/config.html>

removed pytest precommithook. It will become slow over time and also doesn't work when runningin CI since it requires a full .venv

added vulture precommit-hook: <https://github.com/jendrikseipp/vulture>

made pytest accept options in pyproject.toml by using [tool.pytest.ini_options] header instead

added github action for pytest

fix: changed pytest to use importlib as importmode <https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html>

added pytest-watcher <https://pypi.org/project/pytest-watcher/>

added pytest options --durations=5 and --last-failed

added pytest-xdist and added slow test to simulate a workload of tests with slow integration tests

added pyupgrade <https://github.com/asottile/pyupgrade>

added checkmake precommit hook. <https://github.com/mrtazz/checkmake.git>

added gitleaks <https://github.com/gitleaks/gitleaks>

added talisman <https://github.com/thoughtworks/talisman?tab=readme-ov-file#pre-commit>
