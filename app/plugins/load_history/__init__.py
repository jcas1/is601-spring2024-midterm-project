'''Loads Text from savefile.csv to command_history.csv'''
# pylint: disable=missing-class-docstring
from calculator.calc_history import CalcHistory
from app.command_handler import Command

class LoadHistoryCommand(Command):
    def execute(self, *args):
        return CalcHistory.load_history()