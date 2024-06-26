'''App Class, Nessary imports for managing and handling the plugins'''
import sys
import pkgutil
import importlib
import logging
import os
from dotenv import load_dotenv
from calculator.calc_history import CalcHistory
from app.command_handler import CommandHandler, Command


class App:
    '''App Class responsible for managing plugins and handling user interaction'''
    def __init__(self):
        '''Initializes the command handler, and where the plugins should be located'''
        load_dotenv()
        self.command_handler = CommandHandler()
        self.plugins_dir = os.getenv('PLUGINS_DIR', 'app.plugins')
        # Create a logging directory if it doesn't exist
        self.logging_dir = 'logs'
        os.makedirs(self.logging_dir, exist_ok=True)

        self.configure_logging()

        #Makes a CSV folder if one does not exist
        if not os.path.exists('csv'):
            os.makedirs('csv')

        # Initialize CSV file for history
        self.csv_history_manager = CalcHistory()
        self.csv_history_manager.load_history()

    def configure_logging(self):
        '''Initializing the Logs'''
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        log_file = os.path.join(self.logging_dir, 'app.log')

        logging.basicConfig(level=log_level, format=log_format, filename=log_file)

        if os.getenv('LOG_CONSOLE', 'False').lower() == 'true':
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(log_level)
            console_handler.setFormatter(logging.Formatter(log_format))
            logging.getLogger().addHandler(console_handler)

        logging.info("Logging configured with level %s", log_level)

    def load_plugins(self):
        '''Loads plugins from plugins folder'''
        logging.info("Loading plugins from directory: %s", self.plugins_dir)
        for _, plugin_name, is_pkg in pkgutil.iter_modules([self.plugins_dir.replace('.', '/')]):
            if is_pkg:
                # Dynamically import the module based on its path
                module = importlib.import_module(f'{self.plugins_dir}.{plugin_name}')
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                        # Instantiate and register command
                        self.command_handler.register_command(plugin_name, attribute())
                        logging.info("Plugin Loaded: %s", plugin_name)

    def start(self):
        '''Starts the REPL Calculator Program'''
        self.load_plugins()
        logging.info("Application started")
        print("Welcome to the app!")
        while True:
            user_input = input("Enter a command (type 'quit' to exit): ").strip()

            if user_input.lower() == 'quit':
                logging.info("Exiting application")
                sys.exit("Exiting")

            # Split user input into command and arguments
            split_input = user_input.split()
            command_name = split_input[0].lower()
            args = split_input[1:]  # Extract arguments

            try:
                # Convert arguments to appropriate data types (e.g., float)
                args = [float(arg) for arg in args]
            except ValueError:
                logging.error("Invalid input format: %s", args)
                print("Invalid input format. Arguments must be numeric.")
                continue

            try:
                result = self.command_handler.execute_command(command_name, *args)
                logging.info("Command '%s' executed with parameters: %s. Result: %s", command_name, args, result)
                print("Result:", result)
            except ValueError:
                logging.warning("Cannot divide by zero")
                print("Cannot Divide By Zero")
            except TypeError:
                logging.error("Invalid input format: %s", command_name)
                print("Invalid input format")

            try:
                self.csv_history_manager.update_history(command_name, *args, result)
            except TypeError:
                logging.info("CSV only tracking Operations & Operands")
                continue
            except UnboundLocalError:
                continue
