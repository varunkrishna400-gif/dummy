# Simple Python Calculator

A small command-line calculator for basic arithmetic. It supports addition,
subtraction, multiplication, division, floor division, modulo, powers, unary
signs, and parentheses. Expressions are parsed safely; arbitrary Python code is
not executed. The `sqrt(number)` function is also available.

## Run

Requires Python 3.9 or newer. From this folder, run:

```sh
python calculator.py "(12 + 8) / 4"
```

The result is printed to the terminal. For invalid expressions or division by
zero, the calculator prints an error and exits with a nonzero status.

Examples:

```sh
python calculator.py "7 * 6"
python calculator.py "2 ** 8"
python calculator.py "-10 % 3"
python calculator.py "sqrt(81) + 2"
```
