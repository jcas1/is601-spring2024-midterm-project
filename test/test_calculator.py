'''test for the Calculator class'''
from calculator import Calculator
#from calculator.calc_history import CalcHistory

def test_add():
    '''test for calculator add method'''
    assert Calculator.add(4,6) == 10

def test_subtract():
    '''test for calculator subtract method'''
    assert Calculator.subtract(4,6) == -2

def test_multiply():
    '''test for calculator multiple method'''
    assert Calculator.multiply(4,6) == 24

def test_divide():
    '''test for calculator divide method'''
    assert Calculator.divide(3,6) == .5
