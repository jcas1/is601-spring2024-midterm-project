'''Menu Command that displays all avaiable plugins'''
import pkgutil
from app.command_handler import Command

class MenuCommand(Command):
    '''Command to display available menu options'''
    def execute(self):
        '''Executes the menu command'''
        menu_options = self.get_menu_options()
        self.display_menu(menu_options)

    def get_menu_options(self):
        '''Retrieve available menu options from plugins'''
        menu_options = []
        plugins_dir = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_dir.replace('.', '/')]):
            if is_pkg:
                menu_options.append(plugin_name)
        return menu_options

    def display_menu(self, menu_options):
        '''Display the menu options to the user'''
        print("Menu Options:")
        for idx, option in enumerate(menu_options, start=1):
            print(f"{idx}. {option}")
