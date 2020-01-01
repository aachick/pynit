# pynit

`pynit` is a simple tool that allows developers to facilitate the creation of Python projects. To function correctly, users must have a version of `git` installed on their local machine.

## Example

`pynit` is designed to be run from the CLI and can at its most basic, be used as so:

```bash
python -m pynit foobar
```

This will yield the following project structure:

```
../foobar
├── foobar
│   └── __init__.py
├── .git
└── .gitignore
```

A more complete usage example ensues:

```bash
python -m pynit foobar --setup --manifest --readme --license MIT --author me --description 'A simple program' --progv 0.1.0
```

This will yield the following project structure:

```
../foobar
├── LICENSE.txt
├── MANIFEST.in
├── README.md
├── foobar
│   └── __init__.py
├── setup.py
├── .git
└── .gitignore
```

## Dependencies

Whilst the package does not require external dependencies, system calls are made to use `git`, which is therefore required.
