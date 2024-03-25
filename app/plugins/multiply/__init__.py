'''Multiply Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command
from calculator import Calculator

class MultiplyCommand(Command):
    def execute(self, x, y):
        return Calculator.multiply(x, y)
