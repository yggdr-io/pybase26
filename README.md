# base26

This library provides functions for encoding binary data to printable ASCII
characters and decoding such encodings back to binary data.
The algorithm is Base26.

Base26 encoding takes binary data (a byte array) and converts it into a stream
of letters, drawn from a 26-character pool in capital letters,
e.g. byte arrays of 0xA5, 0x05, 0x4B = Base26 encoded value of "TDTTKA".

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
