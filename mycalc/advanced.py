import math

def power(base, exponent):
    """Raise a number to a power."""
    return base ** exponent

def sqrt(x):
    """Square root of a number."""
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)

def factorial(n):
    """Factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

def logarithm(x, base=math.e):
    """Logarithm of x with given base (default: natural log)."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x, base)

def sine(deg):
    """Sine of an angle in degrees."""
    return math.sin(math.radians(deg))

def cosine(deg):
    """Cosine of an angle in degrees."""
    return math.cos(math.radians(deg))

def tangent(deg):
    """Tangent of an angle in degrees."""
    return math.tan(math.radians(deg))
