""" import all the methods from calc_methods"""
from calculator.history_calculations.history_calculations import History


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        History.get_last_calculation_added()
        return True

    @staticmethod
    def addition(*args):
        """ Adds given list of numbers and appends the result to history """
        History.add_addition_to_history(args)
        return True

    @staticmethod
    def subtraction(*args):
        """ Subtracts given list of numbers and appends the result to history """
        History.add_subtraction_to_history(args)
        return True


    @staticmethod
    def multiplication(*args):
        """ Multiplies given list of numbers and appends the result to history """
        History.add_multiplication_to_history(args)
        return True

    @staticmethod
    def division(*args):
        """ Divides given list of numbers and appends the result to history """
        History.add_division_to_history(args)
        return True
