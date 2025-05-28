"""
A simple math operations module to demonstrate Python modules.
"""


def add(x, y):
    """Add two numbers and return the result."""
    return x + y


def subtract(x, y):
    """Subtract y from x and return the result."""
    return x - y


def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y


def divide(x, y):
    """Divide x by y and return the result."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y 

