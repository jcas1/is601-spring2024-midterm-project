# conftest.py
# pylint: disable=line-too-long
# pylint: disable=comparison-with-callable
'''conftest to enable faker'''
from faker import Faker
from calculator.operations import add, subtract, multiply, divide
fake = Faker()

def generate_test_data(num_records):
    '''# Dictionary containing the basic arithmatic opertions'''
    operations = {
        'addition': add,
        'subtraction': subtract,
        'multiplication': multiply,
        'division': divide
    }
    # Generates the test data
    for _ in range (num_records):
        x = fake.random_number(digits = 2)
        y = fake.random_number(digits = 2) if _ % 4 != 3 else fake.random_number(digits = 1)
        operation_name = fake.random_element(elements=list(operations.keys()))
        operation_func = operations[operation_name]

        if operation_func == divide:
            x = 1 if y == 0 else 0

        try:
            if operation_func == divide and y == 0:
                expected = ValueError
            else:
                expected = operation_func(x, y)
        except ZeroDivisionError:
            expected = ZeroDivisionError

        yield x, y, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''Controls the Number of test records to generate'''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''Generates the test data based on the num records'''
    if {"x", "y", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(x, y, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for x, y, op_name, op_func, expected in parameters]
        metafunc.parametrize("x, y, operation, expected", modified_parameters)
