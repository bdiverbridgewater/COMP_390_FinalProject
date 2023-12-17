import os
from io import StringIO

import pytest
from Meteorite_Filter import *
from utility_functions import *


def test_is_file_name():
    """This tests the is_file_name function within the utility_functions module. A boolean is returned based on an
    inputted string. If that string can be used by the open() function in the standard library, then it returns true.
    Otherwise, it returns false"""
    test_file_names = ['henry', 'Q', '123', 'test_file']
    fake_file_names = ['bob', 'Qt', '34_78', 'test', '']

    # Creating some dummy files for test cases asserted to be true
    for file_name in test_file_names:
        new_file = open(file_name, 'a')
        new_file.write("something")
        new_file.close()

    for file_name in test_file_names:
        assert is_file_name(file_name) == True

    for file_name in fake_file_names:
        assert is_file_name(file_name) == False

    # Deleting the dummy file after testing
    for file_name in test_file_names:
        os.remove(file_name)


def test_request_lower_bound(monkeypatch, capfd):
    """testing when the user must input a numerical value to the console. If the input can be casted as a float,
    the function will accept the input. If the input can not be seen as a number, an error message is printed and the
    function returns None"""
    test_filter = Meteorite_Filter()
    failed_test_cases = ['gah;ksld', 'lower bound', 'h', '1h5']
    good_inputs = ['0', '1', '12.34', '17777', '-300']
    for test_input in failed_test_cases:
        simulated_input = StringIO(test_input)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert test_filter.request_lower_bound() is None
        out, err = capfd.readouterr()
        assert out == ('What is the lower bound of your filtering parameter?(inclusive)("Q" to '
                       'quit)\n'
                       f'>>ERROR: "{test_input}" is not a number\n')
    for test_input in good_inputs:
        simulated_input = StringIO(test_input)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert test_filter.request_lower_bound() == float(test_input)
        out, err = capfd.readouterr()
        assert out == ('What is the lower bound of your filtering parameter?(inclusive)("Q" to '
                       'quit)\n'
                       '>>')


def test_request_output_format(monkeypatch, capfd):
    """testing when the user is interacting with the output format menu. Only numbers representing menu options are valid input. All input that can't be read as"""
    test_filter = Meteorite_Filter()
    valid_inputs = ['1', '2', '3']
    failed_inputs = ['one', 'not a number', 'what']
    numbers_not_in_menu = ['5', '6', '59.57', '0']
    for test_input in valid_inputs:
        simulated_input = StringIO(test_input)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert test_filter.request_output_format() == float(test_input)
        out, err = capfd.readouterr()
        assert out == ('What output format would you like to use?\n'
                       '1. print to console\n'
                       '2. write to a text file\n'
                       '3. write to an excel file\n'
                       '4. Quit\n'
                       '>>')
    for test_input in failed_inputs:
        simulated_input = StringIO(test_input)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert test_filter.request_output_format() is None
        out, err = capfd.readouterr()
        assert out == ('What output format would you like to use?\n'
                       '1. print to console\n'
                       '2. write to a text file\n'
                       '3. write to an excel file\n'
                       '4. Quit\n'
                       f'>>ERROR: "{test_input}" is not a valid menu option\n')
    for test_input in numbers_not_in_menu:
        simulated_input = StringIO(test_input)
        monkeypatch.setattr('sys.stdin', simulated_input)
        assert test_filter.request_output_format() == float(test_input)
        out, err = capfd.readouterr()
        assert out == ('What output format would you like to use?\n'
                       '1. print to console\n'
                       '2. write to a text file\n'
                       '3. write to an excel file\n'
                       '4. Quit\n'
                       f'>>ERROR: "{test_input}" is not a valid menu option\n')