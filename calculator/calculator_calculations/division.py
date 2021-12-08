""" Import Calculation Parent Class Constructor """

from calculator.calculator_calculations.calculation import Calculation

# This is division method which inherits the calculation class constructor


class Division(Calculation):
    """ Performs division between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        division_of_values = 1.0
        for value in self.values:
            division_of_values = value / division_of_values
        return division_of_values
