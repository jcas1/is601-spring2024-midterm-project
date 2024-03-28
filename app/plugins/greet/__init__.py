'''Personal Testing To make sure that plugins work as intended'''
from app.command_handler import Command

class GreetCommand(Command):
    '''returns Hello'''
    def execute(self, *args):
        return "Hello"
