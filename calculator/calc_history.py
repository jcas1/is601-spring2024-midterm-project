'''Class that manages the calculator history and function unrelated to arithmetic operation'''
import warnings
import pandas as pd

class CalcHistory:
    '''Manages a history of calculations'''

    csv_path = 'csv/command_history.csv'

    @classmethod
    def get_latest(cls):
        '''Returns the latest calculation history'''
        if not cls.history.empty:
            latest_entry = cls.history.iloc[-1]  # Get the last row of the DataFrame
            operation = latest_entry['Operation']
            operand1 = latest_entry['Operand1']
            operand2 = latest_entry['Operand2']
            result = latest_entry['Result']
            return operation, operand1, operand2, result
        return None

    @classmethod
    def clear_history(cls):
        '''Clears history'''
        cls.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        cls.history.to_csv(cls.csv_path, index=False)

    @classmethod
    def load_history(cls):
        '''Load history from savefile.csv and overwrite command_history.csv'''
        savefile_path = 'csv/savefile.csv'
        try:
            history_df = pd.read_csv(savefile_path)
            cls.history = history_df
            cls.history.to_csv(cls.csv_path, index=False)
            return cls.history
        except FileNotFoundError:
            cls.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
            cls.history.to_csv(cls.csv_path, index=False)
            return cls.history

    @classmethod
    def save_history(cls):
        '''Save history to a new CSV file named savefile.csv'''
        savefile_path = 'csv/savefile.csv'
        cls.history.to_csv(savefile_path, index=False)

    @classmethod
    def update_history(cls, operation, operand1, operand2, result):
        '''Update history'''
        new_entry = pd.DataFrame({'Operation': [operation], 'Operand1': [operand1], 'Operand2': [operand2], 'Result': [result]})
        if not new_entry.dropna().empty:
            # Ignore FutureWarning
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=FutureWarning)
                cls.history = pd.concat([cls.history, new_entry.dropna()], ignore_index=True, sort=False)
            cls.history.to_csv(cls.csv_path, index=False)
        else:
            print("Skipping empty or all-NA entry:", new_entry)
