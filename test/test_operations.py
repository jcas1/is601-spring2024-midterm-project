'''Testing General Operations'''
import pytest
from calculator.operations import add, subtract, multiply, divide
#from calculator import Calculator

def test_add():
    '''test for addition'''
    assert add(4,5) == 9

def test_subtract():
    '''test for subtraction'''
    assert subtract(4,5) == -1

def test_multiply():
    '''test for multiplication'''
    assert multiply(4,5) == 20

def test_divide():
    '''test for division'''
    assert divide(4,5) == 0.8

def test_divide_by_zero():
    '''test for division by zero'''
    with pytest.raises(ValueError):
        divide(4,0)
