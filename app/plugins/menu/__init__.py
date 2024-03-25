'''Multiply Command'''
# pylint: disable=missing-class-docstring
from app.command_handler import Command

class MenuCommand(Command):
    def execute(self, *args):
        print("Available plugins:")
        for plugin_name in args:
            print(f"- {plugin_name}")
