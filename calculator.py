"""A small, safe command-line arithmetic calculator."""

import argparse
import ast
import operator
import sys
import math


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _evaluate(node):
    if isinstance(node, ast.Expression):
        return _evaluate(node.body)
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
        return _BINARY_OPERATORS[type(node.op)](
            _evaluate(node.left), _evaluate(node.right)
        )
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
        return _UNARY_OPERATORS[type(node.op)](_evaluate(node.operand))
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sqrt"
        and len(node.args) == 1
        and not node.keywords
    ):
        value = _evaluate(node.args[0])
        if value < 0:
            raise ValueError("sqrt() requires a non-negative number.")
        return math.sqrt(value)
    raise ValueError("Use numbers and supported arithmetic operators only.")


def calculate(expression):
    """Evaluate an arithmetic expression without executing arbitrary code."""
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid arithmetic expression.") from exc
    return _evaluate(tree)


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate arithmetic expressions; sqrt(number) is also supported."
    )
    parser.add_argument("expression", help='for example: "sqrt(81) + 2"')
    args = parser.parse_args()

    try:
        print(calculate(args.expression))
    except (ValueError, ZeroDivisionError, OverflowError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
