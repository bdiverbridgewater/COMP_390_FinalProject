"""
This module assists with converting a string to an int or
float.
Only the convert_string_to_numerical() function is available to outside files
"""
from datetime import datetime


def _string_is_numerical(in_string):
    """ returns True if the incoming parameter can be converted to float (i.e. is a number)
    returns False otherwise - checks for TypeError and ValueError on incoming value """

    try:
        float(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def convert_string_to_numerical(in_string):
    """ this function converts a string to a numerical value (to either an int or float)
        'None' is returned if the incoming string is not in the form of an int or float """

    if _string_is_numerical(in_string):
        return float(in_string)
    return None


def _insert_none_data(data_list):
    """ converts empty string '' and '\n' elements in the list to 'None' - returns the modified list """

    index_pointer = 0
    for element in data_list:
        # check to see if there is nothing (empty string) or a '\n' for an element
        if element == '' or element == '\n':
            # if an empty string or '\n' is found, replace that element with 'None'
            data_list[index_pointer] = None
        index_pointer += 1
    return data_list


def clean_data_list(data_str):
    """ this function takes a data string as its single parameter - it cleans the data string - removes the newline
    character and splits the data string on the tab separation - this creates a list. This list is then processed
    by replacing all empty strings and '\n' elements with a None value - the clean list is then returned """

    strip_line = data_str.strip('\n')
    # get a tab separated list from the file line
    tab_sep_line = strip_line.split('\t')
    # convert missing data point to None in the list - this applies to '' and '\n' for the missing Counties data
    clean_data = _insert_none_data(tab_sep_line)
    return clean_data


def is_file_name(input_string):
    """checks if a string is the name of a file that can be opened. Returns true if it is. Returns false if it isn't"""
    try:
        test_file = open(input_string)
        test_file.close()
    except OSError:
        return False
    return True


def is_menu_option(read_value, menu):
    """takes a value and checks if its a number corresponding to a menu item. The read_value is meant to start
    at 1, not 0. There isn't a 0 menu option. The menu passed to the function is simply a list with a set length"""
    if not _string_is_numerical(read_value):
        return False
    read_value = convert_string_to_numerical(read_value)
    return len(menu) >= read_value >= 1


def check_for_quit(user_input, quit_options):
    """checks an input string to see if it appears in a list call quit_options. If it is in the list,
    then quit the program"""
    if user_input in quit_options:
        print('Quitting program now...')
        quit()


def get_clean_datetime_string():
    """gets a value representing the current time and converts it to a form that is valid for a file name"""
    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_str = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_str = clean_timestamp_str.replace('.', '_')
    clean_timestamp_str = clean_timestamp_str.replace(' ', '_')
    return clean_timestamp_str
