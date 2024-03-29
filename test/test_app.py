'''Testing for App class'''
from unittest.mock import patch
import pytest
from app import App

@pytest.fixture
def app():
    '''app'''
    return App()

def test_load_plugins(app):
    '''Test to make sure that the plugins load in'''
    # Mock the CommandHandler.register_command method
    with patch.object(app.command_handler, 'register_command') as mock_register_command:
        # Load plugins
        app.load_plugins()

        # Assert that register_command is called with correct arguments
        mock_register_command.assert_called()

def test_start_quit_command(app):
    '''Test quit'''
    # Mock sys.exit()
    with pytest.raises(SystemExit) as e:
        # Mock user input
        with patch('builtins.input', side_effect=['quit']):
            app.start()

    # Check if sys.exit() was called
    assert e.type == SystemExit

@pytest.mark.parametrize("user_input, expected_output", [
    ("add 2 2", "Result: 4.0"),
    ("subtract 2 2", "Result: 0.0"),
    ("multiply 4 2", "Result: 8.0"),
    ("divide 4 2", "Result: 2.0"),
    ("divide 4 0", "Cannot Divide By Zero"),
    ("add 4 a", "Invalid input format"),
    ("add 4", "Invalid input format"),
    ("fake_command 4 3", "Command does not exist")
])

def test_calculations(capfd, app, user_input, expected_output):
    '''Test for various calculations'''
    # Mock user input
    inputs = iter([user_input, "quit"])  # Add enough elements to cover all calls to input()

    # Mock user input
    with patch('builtins.input', side_effect=lambda *args: next(inputs)):
        with pytest.raises(SystemExit):
            app.start()
    captured = capfd.readouterr()
    print("Captured output:", captured.out)  # Print output

    # Check if expected output is present in captured output
    if expected_output:
        assert expected_output in captured.out
    else:
        assert captured.out == ''  # No output expected for quitting the app
