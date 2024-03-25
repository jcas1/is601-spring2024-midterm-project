'''Divide Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, x, y):
        return Calculator.divide(x, y)
