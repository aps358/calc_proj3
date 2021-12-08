""" import all the methods from calc_methods"""
from calculator.calculator_calculations.addition import Addition
from calculator.calculator_calculations.subtraction import Subtraction
from calculator.calculator_calculations.multiplication import Multiplication
from calculator.calculator_calculations.division import Division
from calculator.history_calculations.history_calculations import History


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def add_nums(*args):
        """ Adds given list of numbers and appends the result to history """
        addition = Addition(args).getresult()
        History.add_calculation_to_history(addition)
        return History.get_last_calculation_added()

    @staticmethod
    def subtract_nums(*args):
        """ Subtracts given list of numbers and appends the result to history """
        subtraction = Subtraction(args).getresult()
        History.add_calculation_to_history(subtraction)
        return History.get_last_calculation_added()

    @staticmethod
    def multiply_nums(*args):
        """ Multiplies given list of numbers and appends the result to history """
        multiplication = Multiplication(args).getresult()
        History.add_calculation_to_history(multiplication)
        return History.get_last_calculation_added()

    @staticmethod
    def divide_nums(*args):
        """ Divides given list of numbers and appends the result to history """
        division = Division(args).getresult()
        History.add_calculation_to_history(division)
        return History.get_last_calculation_added()
