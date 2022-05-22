# pybase26

This library provides functions for encoding binary data to printable ASCII
characters and decoding such encodings back to binary data.
The algorithm is Base26.

## Development

Install dependencies

```sh
python -m pip install pip-tools
pip-compile --extra dev pyproject.toml
pip-sync
```

Install base26 package in editable mode

```sh
python -m pip install -e .
```

Run tests

```sh
pytest tests
```
