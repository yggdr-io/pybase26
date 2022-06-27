# base26

[![PyPI](https://img.shields.io/pypi/v/base26)](https://pypi.org/project/base26/)

This library provides functions for encoding binary data to printable ASCII
characters and decoding such encodings back to binary data.
The algorithm is Base26.

Base26 encoding takes binary data (a byte array) and converts it into a stream
of letters, drawn from a 26-character pool in capital letters,
e.g. byte arrays of 0xA5, 0x05, 0x4B = Base26 encoded value of "TDTTKA".

Decoding is the reverse of encoding, taking a string of capital letters
and turning it back into a byte array. The Base26 decoding algorithm
may add an extra 0 byte at the end of the returned payload. The algorithm
should check for this: typically, if the returned payload size is 129
and if it is equal to 0 remove it.

It's similar to Base64 but with a smaller pool of characters.

```text
Base64 = ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Base26 = ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

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
