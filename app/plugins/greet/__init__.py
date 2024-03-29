'''Personal Testing To make sure that plugins work as intended'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command

class GreetCommand(Command):
    '''returns Hello'''
    def execute(self, *args):
        return "Hello"
