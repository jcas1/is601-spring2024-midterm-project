# Midterm Project - [videolink](https://youtu.be/AoIwuHDgTZ4)

## Summary:
This Python Calculator App utilizes a REPL (Read-Evaluate-Print-Loop) command line interface (CLI) to perform basic arithmetic operations such as: add, subtract, multiply and divide.
Capabilities to save, modify and load the history of each properly formed arithmetic operation, each operand and the corresponding result to a .csv file utilizing the Pandas library.
Added app modularity by incorporating the use of a plugin system, allowing for more commands to be seamlessly integrated into the app without modifying the general base of the code.
Incorporated a logging system to log the following relative information.

## Design Patterns Used
### Command Pattern - Utilized in the Command and CommandHandler class
The class Command encapsulates the action to be performed. Its execute() method is a generic method that can be used to perform any command.
The class CommandHandler acts as the invoker holding all the commands, it also registers each command to implement the execute() method
The use of the command handler allows for plugins to seamless added to the app, by implement the command into a method, it can be found by the command handler and registered to be used
[Reference](https://refactoring.guru/design-patterns/command)

### Facade Pattern - Used by the CsvHistory Class
The CsvHistory provided a simplified interface for the use of the Pandas library
Allows for the manipulation of a csv file to be easier
[Reference](https://refactoring.guru/design-patterns/facade)

### Singleton Pattern - Used by the CsvHistory Class
Only one instance of the CsvHistory class can be used at a time to ensure consistency in the csv file
[Reference](https://refactoring.guru/design-patterns/facade)

## Other Practices
### Logging - Used all over the App class
Logging is used to keep track of the following:

    When the app is executed
    The logging level
    Where the plugins are loading in from
    The plugins that properly loaded in
    Which command was executed
    If the command was an operation it will also log the operands and result
    Errors, such as invalid input format
    Warnings, such as divide by zero
    When the app is exiting

Logging is useful when checking for bugs/issues, or can also log if the app is being ‘mis-used’
One example is checking to see if a plugin loaded in properly, if the plugin is not in the log, then there is something wrong with the corresponding plugin program
[Reference](https://betterstack.com/community/guides/logging/logging-best-practices/)

### LYBL - Used in the CommandHandler execute command()
Since the program utilizes the CLI, some users may be unaware of the available commands, the input format, or they may just make a typo.
So by checking to see if a command is in the command dictionary, if it is, then it will execute, if not then it will not execute and inform the user that command is not valid
[Reference](https://realpython.com/python-lbyl-vs-eafp/)


### Example Configurations:

To start type the following into the command line:

    '''
    python main.py
    '''

To find what commands are available use just type into the command line:

    '''
    menu
    '''

The following are the valid operations currently available:

    '''
    add
    subtract
    multiply
    divide
    '''

to perform each operation, simply insert two operands (numbers) after the operation

    '''
    add 2 2
    subtract 7 3
    multiple 2.5 2
    divide 10 2
    '''

The following other commands only require the command name into the command line:

    '''
    greet
    clear_history
    get_latest
    load_history
    save_history
    '''

The last four commands are used to manipulate the .csv file.

### Install
Clone repo
    '''
    pip install -requirement.txt
    '''
### Testing
    '''
    pytest
    pytest --pylint
    pytest --pylint --cov
    pytest --num_records 10
    '''
