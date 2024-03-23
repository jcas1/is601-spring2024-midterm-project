# pylint: disable=line-too-long
# pylint: disable=broad-except
'''Integration Testing'''
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(x, y, operation_name):
    '''Notes'''
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        x_decimal, y_decimal = map(Decimal, [x, y])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {x} {operation_name} {y} is equal to {result(x_decimal, y_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {x} or {y} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    '''Notes'''
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, x, y, operation = sys.argv
    calculate_and_print(x, y, operation)

if __name__ == '__main__':
    main()
