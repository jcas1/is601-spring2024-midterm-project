'''csv_history.py testing'''
import os
import pandas as pd
import pytest
from calculator.csv_history import CsvHistory

@pytest.fixture
def csv_history_path(tmp_path):
    '''Fixture to create a temporary CSV file for testing'''
    csv_file = tmp_path / 'test_history.csv'
    return str(csv_file)

def test_init_creates_new_csv(csv_history_path):
    '''Test if CsvHistory initializes a new CSV file if it doesn't exist'''
    history = CsvHistory(csv_history_path)
    assert os.path.exists(csv_history_path)
    assert len(history.csv_history) == 0

def test_init_loads_existing_csv(csv_history_path):
    '''Test if CsvHistory loads an existing CSV file'''
    # Create a sample CSV file
    sample_data = {'Operation': ['add'], 'Operand1': [2.0], 'Operand2': [2.0], 'Result': [4.0]}
    pd.DataFrame(sample_data).to_csv(csv_history_path, index=False)

    # Initialize CsvHistory and check if it loads the existing CSV
    history = CsvHistory(csv_history_path)
    assert len(history.csv_history) == 1
    assert history.csv_history.equals(pd.DataFrame(sample_data))

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_update_history(csv_history_path):
    '''Test updating the CSV history'''
    # Initialize CsvHistory
    history = CsvHistory(csv_history_path)
    assert len(history.csv_history) == 0

    # Update the history
    history.update_history('add', 2.0, 2.0, 4.0)

    # Check if the CSV has been updated
    updated_data = pd.read_csv(csv_history_path)
    assert len(updated_data) == 1
    assert updated_data.iloc[0]['Operation'] == 'add'
    assert updated_data.iloc[0]['Operand1'] == 2.0
    assert updated_data.iloc[0]['Operand2'] == 2.0
    assert updated_data.iloc[0]['Result'] == 4.0
