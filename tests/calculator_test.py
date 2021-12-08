"""Importing Calculator Class from calculator > main.py for Testing"""
import pprint
import pytest
from calculator.main import Calculator
from calculator.history_calculations.history_calculations import History

# pylint: disable=unused-argument,redefined-outer-name


# This is called a fixture and it runs each time you pass it to a test
@pytest.fixture
def clear_history():
    """ Clears history """
    History.clear_history()


def test_calculator_add(clear_history):
    """ To check if calculator addition result is correct """
    assert Calculator.add_nums(10.0, 20.0, 30.0) == 60.0
    assert Calculator.add_nums(10.0, 20.0) == 30.0
    assert History.get_calculation_count() == 2
    assert History.get_first_calculation_history() == 60.0
    assert History.get_last_calculation_added() == 30.0
    pprint.pprint(History.history)


def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    assert Calculator.subtract_nums(10.0, 20.0) == -30.0


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    assert Calculator.multiply_nums(10.0, 20.0) == 200.0


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    assert Calculator.divide_nums(20.0, 20.0) == 1.0
