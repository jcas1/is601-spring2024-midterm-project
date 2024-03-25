'''Add Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, x, y):
        return Calculator.add(x, y)
