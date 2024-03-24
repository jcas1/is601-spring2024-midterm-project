'''App Class, Nessary imports for managing and handling the plugins'''
import sys
import pkgutil
import importlib
from app.command_handler import CommandHandler, Command

class App:
    '''App Class responsible for managing plygins and handling user interaction'''
    def __init__(self):
        '''Initializes the command handler, and where the plugins should be located'''
        self.command_handler = CommandHandler()
        self.plugins_dir = 'app.plugins'

    def load_plugins(self):
        '''Loads plugings from plugins folder'''
        for _, plugin_name, is_pkg in pkgutil.iter_modules([self.plugins_dir.replace('.', '/')]):
            if is_pkg:
                # Dynamically import the module based on its path
                module = importlib.import_module(f'{self.plugins_dir}.{plugin_name}')
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                    # Instantiate and register command
                        self.command_handler.register_command(plugin_name, attribute())

    def start(self):
        '''Starts the REPL Calculator Program'''
        self.load_plugins()
        print("Welcome to the app!")
        while True:
            user_input = input("Enter a command (type 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                sys.exit("Exiting")
            try:
                command_name, x, y = user_input.split()
                x = float(x)
                y = float(y)
            except ValueError:
                print("Invalid input format. Please enter [operation x y] \n x & y must be numbers.")
                continue

            result = self.command_handler.execute_command(command_name, x, y)
            print("Result:", result)
