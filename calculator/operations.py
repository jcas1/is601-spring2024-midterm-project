'''Basic Arithmetic Operations'''

def add(x,y):
    '''Basic Addition Operation'''
    return x + y

def subtract(x,y):
    '''Basic Subtraction Operation'''
    return x - y

def multiply(x,y):
    '''Basic Multiplication Operation'''
    return x * y

def divide(x,y):
    '''
    Basic Division Operation

    Accounts and prevents division by zero    
    '''
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
