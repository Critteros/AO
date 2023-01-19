# Project for AO

### Simple GUI application classifying images to 5 groups:
* Forest
* Desert
* Glacier
* Mountain
* Coast

## Installation:
* Install requirements using:
```
pip install -r requirements.txt
```
* Download model from https://drive.google.com/drive/folders/1Rq7dmWzzOwnZQHjA3Lb1FVL6rGEEaOAI?usp=sharing and paste it into project folder
* Run application using
```
python3 ao
```


## Installation for development:
* have Win11 and WSL or Win10 and patience
* install `PyCharm`
* install `pyenv` from https://github.com/pyenv/pyenv#automatic-installer (Remember to paste commands to `.bashrc`)
* install libs `libssl-dev`, `libsqlite3-dev`, `libffi-dev`, `libbz2-dev`
* run `$ pyenv install 3.10.8` 
* run `$ pyenv virtualenv 3.10.8 AO`
* install `poetry` (install `pipx` and then `pipx poetry`)
* `$ exec bash`
* clone repo and cd into it
* `$ poetry config virtualenvs.in-project true`
* `$ poetry config virtualenvs.prefer-active-python true`
* `pyenv local AO` 
* add new interpreter to PyCharm and set path as `/home/<user>/.pyenv/versions/3.10.8/envs/AO/bin/python`
* `$ poetry install`
* If you survived to this moment congratulations and good night :)