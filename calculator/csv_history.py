'''Class used for CSV file management'''
import os
import pandas as pd

class CsvHistory:
    '''This class meant to update the CSV file based on the users inputs'''
    def __init__(self, csv_history_path):
        '''Initialize CSV file for command history'''
        self.csv_history_path = csv_history_path
        if not os.path.exists(self.csv_history_path):
            # Create new DataFrame if CSV file doesn't exist
            columns = ['Operation', 'Operand1', 'Operand2', 'Result']
            self.csv_history = pd.DataFrame(columns=columns)
            self.csv_history.to_csv(self.csv_history_path, index=False)
        else:
            # Load existing CSV file into DataFrame
            self.csv_history = pd.read_csv(self.csv_history_path)

    def update_history(self, operation, operand1, operand2, result):
        '''Update CSV file for command history'''
        new_entry = pd.DataFrame({'Operation': [operation], 'Operand1': [operand1], 'Operand2': [operand2], 'Result': [result]})
        # Check if new_entry is not empty or all-NA
        if not new_entry.dropna().empty:
            self.csv_history = pd.concat([self.csv_history, new_entry.dropna()], ignore_index=True, sort=False)
            self.csv_history.to_csv(self.csv_history_path, index=False)
        else:
            print("Skipping empty or all-NA entry:", new_entry)
