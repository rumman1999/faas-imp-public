from mycalc import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5
