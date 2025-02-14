# uv-cookiecutter-test

[![Release](https://img.shields.io/github/v/release/Shubxam/uv-cookiecutter-test)](https://img.shields.io/github/v/release/Shubxam/uv-cookiecutter-test)
[![Build status](https://img.shields.io/github/actions/workflow/status/Shubxam/uv-cookiecutter-test/main.yml?branch=main)](https://github.com/Shubxam/uv-cookiecutter-test/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/Shubxam/uv-cookiecutter-test/branch/main/graph/badge.svg)](https://codecov.io/gh/Shubxam/uv-cookiecutter-test)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Shubxam/uv-cookiecutter-test)](https://img.shields.io/github/commit-activity/m/Shubxam/uv-cookiecutter-test)
[![License](https://img.shields.io/github/license/Shubxam/uv-cookiecutter-test)](https://img.shields.io/github/license/Shubxam/uv-cookiecutter-test)

This is a template repository for Python projects that use uv for their dependency management.

- **Github repository**: <https://github.com/Shubxam/uv-cookiecutter-test/>
- **Documentation** <https://Shubxam.github.io/uv-cookiecutter-test/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:Shubxam/uv-cookiecutter-test.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
