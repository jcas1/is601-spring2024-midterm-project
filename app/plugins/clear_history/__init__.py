'''Get Latest Calculation from History'''
# pylint: disable=missing-class-docstring
from calculator.calc_history import CalcHistory
from app.command_handler import Command

class ClearHistoryCommand(Command):
    def execute(self, *args):
        return CalcHistory.clear_history()
