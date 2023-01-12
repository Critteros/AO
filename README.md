# Project for AO

## Instalation:
* install `PyCharm`
* install `WSL`
* install `pyenv` from https://github.com/pyenv/pyenv#automatic-installer (Remember to paste commands to `.bashrc`)
* install libs `libssl-dev`, `libsqlite3-dev`, `libffi-dev`
* run `$ pyenv install 3.10.8` 
* run `$ pyenv virtualenv 3.10.8 AO`
* install `poetry` (install `pipx` and then `pipx poetry`)
* `$ exec bash`
* clone repo and cd into it
* run `$ poetry config virtualenvs.in-project true`
* `$ poetry config virtualenvs.prefer-active-python true`
* `pyenv local AO` 
* add new interpreter to PyCharm and set path as `/home/<user>/.pyenv/versions/3.10.8/envs/AO/bin/python`
* `$ poetry install`
* If you survived to this moment congratulations and good night :)