'''Test for calculation.py'''
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

#pytest,mark,paraneterize is removed due to conftest

def test_calculation(x, y, operation, expected):
    '''using the parametized data to test for multiple operations'''
    calc = Calculation.create(x, y, operation)
    assert calc.perform() == expected

def test_calculation_divide_by_zero():
    '''testing division by zero case'''
    calc = Calculation.create(10, 0, divide)
    with pytest.raises(ValueError):
        calc.perform()
