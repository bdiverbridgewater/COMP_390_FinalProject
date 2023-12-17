"""This module configures the filtering settings as set by the user and then filters a list of meteorites based on
those settings. The filtered list can then be output in 3 ways according to user input"""
from Meteorite import *
from utility_functions import *
from xlwt import Workbook


class Meteorite_Filter:
    """a meteorite_filter object is used to perform the filtering on a list of meteorites. This class collects the
    initial list of metorites from a file and outputs a filtered list of meteorites"""
    table_header = 'name	id	nametype	recclass	mass (g)	fall	year	reclat	reclong	GeoLocation	States	Counties'
    attribute_name_list = ['name', 'id', 'nametype', 'recclass', 'mass (g)', 'fall', 'year', 'reclat', 'reclong',
                           'GeoLocation', 'States', 'Counties']
    filtering_options = ['mass', 'year']
    output_format_options = ['terminal', 'text file', 'excel file']
    accepted_file_modes = ['r', 'w', 'x', 'a']
    file_name_prompt = 'Enter the name of a file containing meteorite data that you would like filtered, with file extension included(ex: "file_name.txt")\nEnter ">q" or ">Q" to quit\n>>'
    file_mode_prompt = 'What mode would you like to open the file with?\n"r" - open for reading(default)\n"w" - open for writing, truncating the file first. (WARNING: this mode will delete the contents of an existing file!)\n"x" - open for exclusive creation, failing if the file already exists\n"a" - open for writing, appending to the end of file if it exists\nEnter ">q" or ">Q" to quit\n>>'
    filtering_parameter_prompt = 'What parameter would you like to filter the meteorites by?\n1. Mass\n2. Year\n3. Quit\n>>'
    lower_bound_prompt = '''What is the lower bound of your filtering parameter?(inclusive)("Q" to quit)\n>>'''
    upper_bound_prompt = '''What is the upper bound of your filtering parameter?(inclusive)("Q" to quit)\n>>'''
    output_format_prompt = 'What output format would you like to use?\n1. print to console\n2. write to a text file\n3. write to an excel file\n4. Quit\n>>'

    def __init__(self):
        """The class variables are used across many different methods within Meteorite_Filter and are better placed
        here than being passed around as parameters. This includes all the variables containing user input that must
        all ultimately be used for the filtering process"""
        self.user_input = None
        self.valid_input = None
        self.meteorite_list = []
        self.filtered_list = []
        self.file_name = None
        self.file_mode = None
        self.filtering_parameter = None
        self.lower_bound = None
        self.upper_bound = None
        self.output_format = None

    def get_input_from_user(self):
        """All information that is needed from the user for the filtering program to run is collected here.
        This function will never complete execution until there is valid input for every user input variable,
        fetching new input when invalid input is given"""
        self.file_name = self.get_file_name_from_user()
        self.file_mode = self.get_file_mode_from_user()
        self.filtering_parameter = self.get_filtering_parameter_from_user()
        self.lower_bound = self.get_lower_bound_from_user()
        self.upper_bound = self.get_upper_bound_from_user()
        self.output_format = self.get_output_format_from_user()

    def get_file_name_from_user(self):
        """Prompts the user for a file name that contains meteorite data. Returns a string that can be used as a
        file name. If the string inputted by the user is not an openable file, the user is reprompted for a new string"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_file_name()
        print(f'File name set: {user_input}')
        return user_input

    def request_file_name(self):
        """A single request for a file name that is looped until valid_input within get_file_name_from_user().
        Input is checked for an exit code and an error message is printed in the case of invalid input"""
        quit_options = ['>q', '>Q']
        user_input = input(self.file_name_prompt)
        check_for_quit(user_input, quit_options)
        self.valid_input = is_file_name(user_input)
        if not self.valid_input:
            print(f'ERROR: "{user_input}" is not a valid file name')
        return user_input

    def get_file_mode_from_user(self):
        """requests a file mode input from the user indefinitely until a valid file mode is inputted in the form of a
        single character"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_file_mode()
        print(f'File mode set: {user_input}')
        return user_input

    def request_file_mode(self):
        """A single request for file mode input, checking for a quit command and rejecting all invalid inputs
        with an error message"""
        quit_options = ['>q', '>Q']
        user_input = input(self.file_mode_prompt)
        check_for_quit(user_input, quit_options)
        self.valid_input = user_input in Meteorite_Filter.accepted_file_modes
        if not self.valid_input:
            print(f'ERROR: "{user_input}" is not a valid file mode')
        return user_input

    def get_filtering_parameter_from_user(self):
        """Asks the user to input a number from the menu in the given prompt and keeps asking until a valid number is
        entered. Returns the filtering parameter corresponding to the number entered"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_filtering_parameter()
        filtering_parameter = Meteorite_Filter.filtering_options[int(user_input) - 1]
        print(f'Filtering parameter set: {filtering_parameter}')
        return filtering_parameter

    def request_filtering_parameter(self):
        """A single request for the filtering parameter option. Checks for quit command and rejects invalid input
        with an error message"""
        quit_options = [str(len(Meteorite_Filter.filtering_options) + 1)]
        raw_user_input = input(self.filtering_parameter_prompt)
        check_for_quit(raw_user_input, quit_options)
        user_input = convert_string_to_numerical(raw_user_input)
        self.valid_input = is_menu_option(user_input, Meteorite_Filter.filtering_options)
        if not self.valid_input:
            print(f'ERROR: "{raw_user_input}" is not a valid menu option')
        return user_input

    def get_lower_bound_from_user(self):
        """prompts the user for a number to use as the lower bound during filtering. Loops until a number is given"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_lower_bound()
        print(f'Lower bound set: {user_input}')
        return user_input

    def request_lower_bound(self):
        """a single request for the lower bound from the user. Checks for a quit command.
        Prints error message on invalid input"""
        quit_options = ['q', 'Q']
        raw_user_input = input(self.lower_bound_prompt)
        check_for_quit(raw_user_input, quit_options)
        user_input = convert_string_to_numerical(raw_user_input)
        self.valid_input = user_input is not None
        if not self.valid_input:
            print(f'ERROR: "{raw_user_input}" is not a number')
        return user_input

    def get_upper_bound_from_user(self):
        """asks the user for a number to use as the upper bound during filtering until a valid number is given"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_upper_bound()
        print(f'Upper bound set: {user_input}')
        return user_input

    def request_upper_bound(self):
        """A single request for upper bound value. Checks for a quit command and valid input.
        Prints an error message when invalid"""
        quit_options = ['q', 'Q']
        raw_user_input = input(self.upper_bound_prompt)
        check_for_quit(raw_user_input, quit_options)
        user_input = convert_string_to_numerical(raw_user_input)
        self.valid_input = user_input is not None
        if not self.valid_input:
            print(f'ERROR: "{raw_user_input}" is not a number')
        return user_input

    def get_output_format_from_user(self):
        """Asks the user to select an output format from a set of menu options by inputting the corresponding integer.
        Loops until a valid integer is entered. Returns the output format as a string"""
        user_input = None
        self.valid_input = False
        while not self.valid_input:
            user_input = self.request_output_format()
        output_format = Meteorite_Filter.output_format_options[int(user_input) - 1]
        print(f'Output format set: {output_format}')
        return output_format

    def request_output_format(self):
        """A single request for the output format from a menu prompt. Only numbers in the prompt menu are valid input.
        The last menu option quits the program"""
        quit_options = [str(len(Meteorite_Filter.output_format_options) + 1)]
        raw_user_input = input(self.output_format_prompt)
        check_for_quit(raw_user_input, quit_options)
        user_input = convert_string_to_numerical(raw_user_input)
        self.valid_input = user_input is not None and is_menu_option(user_input, Meteorite_Filter.output_format_options)
        if not self.valid_input:
            print(f'ERROR: "{raw_user_input}" is not a valid menu option')
        return user_input

    def create_meteorite_list(self):
        """Uses the set file name and file mode to open a text file and read it for meteorite data.
        Creates a list containing all meteorites it finds as meteorite objects"""
        meteorite_file = open(self.file_name, self.file_mode)
        # This stray readline function is here to skip over the header in the text file and immediately read the data
        meteorite_file.readline()
        for line in meteorite_file:
            meteorite = Meteorite()
            meteorite.set_meteorite_from_string(line)
            self.meteorite_list.append(meteorite)

    def filter_meteorite_list(self):
        """Creates a new list of meteorites called filtered_list that consists only of meteorites from meteorite_list
        that fit the filtering criteria"""
        for meteorite in self.meteorite_list:
            if meteorite.mass is not None and self.filtering_parameter == 'mass' and self.lower_bound <= meteorite.mass < self.upper_bound:
                self.filtered_list.append(meteorite)
            elif meteorite.year is not None and self.filtering_parameter == 'year' and self.lower_bound <= meteorite.year < self.upper_bound:
                self.filtered_list.append(meteorite)

    def create_text_file(self):
        """creates a new text file in the project folder named based on the exact time of creation, containing the
        filtering results. This text file has the same format as the original meteorite_landings.txt file and can
        therefore be used as a new data file for another run of the filtering program"""
        clean_timestamp_str = get_clean_datetime_string()
        output_file = open(f'{clean_timestamp_str}.txt', 'a')
        output_file.write(f'{self.table_header} + \n')
        for meteorite in self.filtered_list:
            for attribute in meteorite.attribute_list:
                output_file.write(f'{attribute}\t')
            output_file.write('\n')
        print(f'\n\033Filtered output sent to "{clean_timestamp_str}.txt"\033')

    def create_excel_file(self):
        """sends the filtered list of meteorites to a new excel file in the project folder, named based on time of
        creation. Each attribute is contained within a single cell in the excel document"""
        excel_workbook = Workbook()
        filtered_data_sheet = excel_workbook.add_sheet('filteredMeteoriteData')
        self.label_excel_columns(filtered_data_sheet)
        self.write_data_to_excel(filtered_data_sheet)
        clean_timestamp_str = get_clean_datetime_string()
        excel_workbook.save(f'{clean_timestamp_str}.xls')
        print(f'\n\033Filtered output sent to "{clean_timestamp_str}.xls"\033')

    def label_excel_columns(self, excel_sheet):
        """writes a header into the excel document on the first row. Each column will be named for the attribute
        data it contains"""
        index = 0
        for name in Meteorite_Filter.attribute_name_list:
            excel_sheet.write(0, index, name)
            index = index + 1

    def write_data_to_excel(self, excel_sheet):
        """fills the excel document with meteorite data from the filtered_list. Each row corresponds
        to a single meteorite"""
        for index in range(len(self.filtered_list)):
            meteorite = self.filtered_list[index]
            attribute_list = meteorite.attribute_list
            for attribute_index in range(len(attribute_list)):
                excel_sheet.write(index + 1, attribute_index, attribute_list[attribute_index])

    def output_meteorite_list(self):
        """Takes a different action depending on the selected output format after filtering is complete. All options
        are different ways of writing the data entered in the filtered_list"""
        if self.output_format == 'terminal':
            self.print_results_to_console()
        elif self.output_format == 'text file':
            self.create_text_file()
        elif self.output_format == 'excel file':
            self.create_excel_file()
        else:
            print('could not output filtered meteorite list')

    def print_results_to_console(self):
        """prints the meteorite data for each meteorite in filtered_list neatly to the console with a table header"""
        spacing = 30
        for name in Meteorite_Filter.attribute_name_list:
            print(f'{name:<{spacing}}', end='')
        print('\n' + '=' * spacing * 10)
        for meteorite in self.filtered_list:
            for attribute in meteorite.attribute_list:
                if attribute is None:
                    attribute = ''
                print(f'{attribute:<{spacing}}', end='')
            print()
