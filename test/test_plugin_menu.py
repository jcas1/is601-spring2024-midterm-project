'''Test for menu plugin'''
from app.plugins.menu import MenuCommand

def test_menu(capsys):
    '''
    checking to see if all currently available commands are shown
    if plugin is added, this test would need to be adjusted as well
    '''
    menu = MenuCommand()
    menu.execute()
    captured = capsys.readouterr()

    assert "Menu Options:" in captured.out
    menu_options = menu.get_menu_options()
    assert len(menu_options) == 10
    assert "add" in menu_options
    assert "clear_history" in menu_options
    assert "divide" in menu_options
    assert "get_latest" in menu_options
    assert "greet" in menu_options
    assert "load_history" in menu_options
    assert "menu" in menu_options
    assert "multiply" in menu_options
    assert "save_history" in menu_options
    assert "subtract" in menu_options
