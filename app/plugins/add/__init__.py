'''Add Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, *args):
        return Calculator.add(*args)
