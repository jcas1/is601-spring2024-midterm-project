#pylint: disable=unused-import
'''
Calculation Class
Used to encapsulate the operands and operation 
'''
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    '''Calculation class'''
    def __init__(self, x, y, operation):
        '''
        Initializes the calculation class
        where x is the first operand,
        y is the second operand,
        and any operation too allow for flexiblity 
        '''
        self.x = x
        self.y = y
        self.operation = operation

    @staticmethod
    def create(x, y, operation):
        '''
        an alternative method to create a new instance of the calculation class,
        without creating the calculation class first
        '''
        return Calculation(x, y, operation)

    def perform(self):
        '''performs the desired operation with the specificed operands'''
        return self.operation(self.x, self.y)
