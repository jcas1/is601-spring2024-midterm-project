'''Test Greet Command'''
from app.plugins.greet import GreetCommand

def test_greet_command():
    '''Test Greet Command'''
    greet = GreetCommand()
    result = greet.execute()
    assert result == "Hello"
