'''Calculator class that performs the calculations and stores them'''
from calculator.calculation import Calculation
from calculator.calc_history import CalcHistory
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Calculator class'''
    @staticmethod
    def calculate(x, y, operation):
        '''
        takes two operands, and one operation
        will perform the calculation and save it as well
        '''
        calc = Calculation(x, y, operation)
        return calc.perform()

    @staticmethod
    def add(x, y):
        '''
        Utilized the calculate method to specifically add two numbers
        and store the calculation
        '''
        return Calculator.calculate(x, y, add)

    @staticmethod
    def subtract(x, y):
        '''
        Utilized the calculate method to specifically subtract two numbers
        and store the calculation
        '''
        return Calculator.calculate(x, y, subtract)

    @staticmethod
    def multiply(x, y):
        '''
        Utilized the calculate method to specifically multiply two numbers
        and store the calculation
        '''
        return Calculator.calculate(x, y, multiply)

    @staticmethod
    def divide(x, y):
        '''
        Utilized the calculate method to specifically divide two numbers
        and store the calculation
        '''
        return Calculator.calculate(x, y, divide)
