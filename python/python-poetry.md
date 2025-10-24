## Poetry

### Error: Python packaging tool 'setuptools' not found
https://stackoverflow.com/questions/75307814/error-python-packaging-tool-setuptools-not-found

Also related: https://stackoverflow.com/questions/7446187/no-module-named-pkg-resources
https://python-poetry.org/blog/announcing-poetry-1.7.0/#:~:text=Further%2C%20setuptools%20and%20wheel%20will,explicit%20dependency%20in%20your%20pyproject.


Solution: 
```
poetry add --group dev setuptools
```

## Parse version from pyproject.toml
https://stackoverflow.com/questions/71592060/makefile-how-should-i-extract-the-version-number-embedded-in-pyproject-toml

```
VERSION := $(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)
```

## Poetry not always finds latest version from PyPi
https://github.com/python-poetry/poetry/issues/3543

```
poetry add cdsw-job-launcher=$new_version --no-cache
```