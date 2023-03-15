# Basic Repo Cookiecutter

This is a basic template repository for a python project. 

You can clone this repo by running `$ cookiecutter https://github.com/freemocap/basic_repo_cookiecutter.git` in your terminal. On running that command, you'll be prompted to enter the project name, project version, author, email, and the github username of the repo owner. This should fill in all of your information into the relevant places in the repo template, allowing you to start using it for your new project.

The [command line options](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/cli_options.html#command-line-options) for cookie cutter have additional options when cloning this repo.

## Publishing to PyPi (to make it pip installable)

NOTE - These instructions are undertested

You'll need to create a PyPi account and then create an API token for the Github Action configured in the file: .github/workflows/publish_to_pypi_when_new_tag_is_pushed_to_main.yml

These instructions may help you set that up! https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
