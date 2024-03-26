#pylint: disable=unnecessary-pass
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
        Utilizing Easier to Ask for Forgiveness than Permission (EAFP)

        Since the commands for the calculator are straight forward, the user will likely not make a mistake
        However, in case that the user does, nothing would occur
        '''
        try:
            return self.commands[command].execute(*args)
        except KeyError:
            print("Command does not exist")
            return None

    def get_registered_commands(self):
        '''Returns a list of registered command names'''
        return list(self.commands.keys())
