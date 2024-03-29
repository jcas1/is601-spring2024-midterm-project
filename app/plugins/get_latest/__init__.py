'''Get Latest Calculation from CSV History'''
# pylint: disable=missing-class-docstring
from calculator.calc_history import CalcHistory
from app.command_handler import Command

class GetLastestCommand(Command):
    def execute(self, *args):
        return CalcHistory.get_latest()
