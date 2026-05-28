## License

Nickel is licensed under the Apache License 2.0 with additional attribution notice requirements. See the `LICENSE` and `NOTICE` files. Original author credit must be preserved when using or redistributing this code.


# Nickel

Nickel is a small custom programming language interpreter in development written in Python. It supports basic arithmetic, variable declaration, and variable reassignment, with source files using the `.nc` extension.

## Features

- Supports numeric literals.
- Supports arithmetic operators: `+`, `-`, `*`, `/`.
- Supports grouping with parentheses.
- Supports variable declaration with `let`.
- Supports reassignment with `name = expression`.
- Prints evaluated results and current variable state for debugging.

## File Type

Nickel source files use the `.nc` extension.

**Important:** `.nc` files will not be uploaded.

## Requirements

- Python 3.x

## How to Run

From the project folder, run:

```bash
python Nickel.py main.nc
```

You can replace `main.nc` with any other Nickel source file.

## Example

Example Nickel code:

```nc
let x = 5
x = 6
x = 7
```

Example output:

```text
NumNode(5.0)
{'x': 5.0}
NumNode(6.0)
{'x': 6.0}
NumNode(7.0)
{'x': 7.0}
```

## Language Syntax

### Variable Declaration

```nc
let x = 5
```

Creates a new variable named `x` and stores the value `5`.

### Variable Reassignment

```nc
x = 10
```

Updates the existing value of `x`.

### Expressions

```nc
let y = 2 + 3 * 4
```

Nickel evaluates arithmetic expressions with operator precedence.

## Project Structure

```text
Nickel/
├── Nickel.py
├── main.nc
└── README.md
```

## Notes
- Nickel is in current development
- The interpreter currently prints parsed nodes and the environment for debugging.
- Assignment handling depends on correct tokenization of `=` and correct parser branching.
- `.nc` files are meant to be local source files for Nickel programs and will not be uploaded.

## Future Improvements

- Add support for error messages with line numbers.
- Add better variable lookup inside expressions.
- Add support for strings and comments.
- Add a cleaner REPL mode.
- Add unit tests.

## License

Add your preferred license here.
