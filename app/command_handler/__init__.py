#pylint: disable=unnecessary-pass
#pylint: disable=no-else-return
'''CommandHandler'''
from abc import ABC, abstractmethod

class Command(ABC):
    '''
    Base class for commands includes a execute method with two parameters 
    '''
    @abstractmethod
    def execute(self, *args):
        '''generic execute'''
        pass

class CommandHandler:
    '''Handler class used to manage and execute registerd commands'''

    def __init__(self):
        '''Initializes itself with a blank dictionary'''
        self.commands = {}

    def register_command(self, name: str, command):
        '''Used to register a command with a given name'''
        self.commands[name] = command

    def execute_command(self, command, *args):
        '''
        Utilizing Look Before You Leap (LBYL) principle

        Check if the specified command exists before attempting to execute it.
        '''
        if command in self.commands:
            return self.commands[command].execute(*args)
        else:
            print("Command does not exist")
            return None
