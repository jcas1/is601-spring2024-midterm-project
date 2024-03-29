'''Save Calculations from command_history.csv into another savefile.csv'''
# pylint: disable=missing-class-docstring
from calculator.calc_history import CalcHistory
from app.command_handler import Command

class SaveHistoryCommand(Command):
    def execute(self, *args):
        return CalcHistory.save_history()
