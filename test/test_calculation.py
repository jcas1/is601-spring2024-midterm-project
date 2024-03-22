'''Test for calculation.py'''
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y, operation, expected", [
    (4, 5, add, 9),  # Test addition
    (4, 5, subtract, -1), # Test subtraction
    (4, 5, multiply, 20), # Test multiplication
    (4, 5, divide, 0.8), # Test division
])

def test_calculation(x, y, operation, expected):
    '''using the parametized data to test for multiple operations'''
    calc = Calculation.create(x, y, operation)
    assert calc.perform() == expected

def test_calculation_divide_by_zero():
    '''testing division by zero case'''
    calc = Calculation.create(10, 0, divide)
    with pytest.raises(ValueError):
        calc.perform()
