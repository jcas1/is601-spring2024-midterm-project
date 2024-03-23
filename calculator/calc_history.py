'''Class that manages the calculator history and function unrelated to arithmetic operation'''
class CalcHistory:
    '''Manages a history of calculations'''

    history = []

    @classmethod
    def add_calc(cls, calculation):
        '''Appends the last calculation to history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        '''Returns history'''
        return cls.history

    @classmethod
    def get_latest(cls):
        '''Returns the lastest calculation history'''
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def clear_history(cls):
        '''Clears history'''
        cls.history.clear()
        #print("History cleared")
