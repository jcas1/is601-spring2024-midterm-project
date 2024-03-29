'''test for calc_history'''
#pylint: disable=redefined-outer-name
#pylint: disable=unused-argument
import os
import pandas as pd
from calculator.calc_history import CalcHistory
from app.plugins.get_latest import GetLastestCommand
from app.plugins.save_history import SaveHistoryCommand
from app.plugins.clear_history import ClearHistoryCommand
from app.plugins.load_history import LoadHistoryCommand

def test_get_latest():
    '''Creates a sample data set and confirms that its the latest'''
    history_df = pd.DataFrame({'Operation': ['add'], 'Operand1': [2.0], 'Operand2': [2.0], 'Result': [4.0]})
    CalcHistory.history = history_df
    get_latest_command = GetLastestCommand()
    result = get_latest_command.execute()
    assert result == ('add', 2.0, 2.0, 4.0)

def test_get_latest_no_history():
    '''Creates a sample data set and confirms that its the latest'''
    history_df = pd.DataFrame({'Operation': [], 'Operand1': [], 'Operand2': [], 'Result': []})
    CalcHistory.history = history_df
    get_latest_command = GetLastestCommand()
    result = get_latest_command.execute()
    assert result is None

def test_clear_history():
    '''Adds data to command_history.csv and then clears it to confirm'''
    CalcHistory.history = pd.DataFrame({'Operation': ['add'], 'Operand1': [2.0], 'Operand2': [2.0], 'Result': [4.0]})
    ClearHistoryCommand().execute()
    assert CalcHistory.history.empty

def test_load_history():
    '''
    Creates sample data and saves it to savefile.csv then loads it back to the 
    to the command_history.csv
    '''
    savefile_df = pd.DataFrame({'Operation': ['subtract'], 'Operand1': [5.0], 'Operand2': [3.0], 'Result': [2.0]})
    savefile_df.to_csv('csv/savefile.csv', index=False)
    load_history_command = LoadHistoryCommand()
    result = load_history_command.execute()
    assert isinstance(result, pd.DataFrame)
    assert result.equals(savefile_df)

def test_save_history():
    '''
    Creates sample data and saves it to savefile.csv then checks if corresdponding data is the 
    savefile.csv
    '''
    history_df = pd.DataFrame({'Operation': ['multiply'], 'Operand1': [4.0], 'Operand2': [3.0], 'Result': [12.0]})
    CalcHistory.history = history_df
    save_history_command = SaveHistoryCommand()
    save_history_command.execute()
    assert os.path.exists('csv/savefile.csv')
    saved_df = pd.read_csv('csv/savefile.csv')
    assert saved_df.equals(history_df)
