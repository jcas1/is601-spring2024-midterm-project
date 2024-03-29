'''Subtract Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command
from calculator import Calculator

class SubtractCommand(Command):
    def execute(self, x, y):
        return Calculator.subtract(x, y)
