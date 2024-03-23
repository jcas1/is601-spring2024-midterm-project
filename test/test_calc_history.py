'''test for calc_history'''
#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument
import pytest
from calculator.calc_history import CalcHistory
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def test_setup():
    '''Setup test data to test calc history'''
    CalcHistory.clear_history()
    CalcHistory.add_calc(Calculation(3, 4, add))
    CalcHistory.add_calc(Calculation(3, 4, subtract))
    CalcHistory.add_calc(Calculation(3, 4, multiply))
    CalcHistory.add_calc(Calculation(3, 4, divide))

def test_add_history(test_setup):
    '''test to see if get history works'''
    CalcHistory.add_calc(Calculation(4, 5, add))
    assert CalcHistory.get_latest().x == 4 and CalcHistory.get_latest().y == 5

def test_get_history(test_setup):
    '''test to see if get history works'''
    assert len(CalcHistory.get_history()) == 4

def test_get_latest(test_setup):
    '''test to see if get history works'''
    assert CalcHistory.get_latest().x == 3 and CalcHistory.get_latest().y == 4

def test_clear_history(test_setup):
    '''test to see if clear history works'''
    assert CalcHistory.clear_history() is None

def test_get_latest_no_history(test_setup):
    '''test to see if get history works'''
    CalcHistory.clear_history()
    assert CalcHistory.get_latest() is None
