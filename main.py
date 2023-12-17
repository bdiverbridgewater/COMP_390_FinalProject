'''This is the main module of the program. Most of the computation is done by the Meteorite_Filter module. This module
prints a welcome and exit message along with starting execution'''
from Meteorite_Filter import *

welcome_message = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the meteorite filtering program. This program reads a text file containing meteorite data and outputs a 
list of meteorites filtered on a either a range of mass or year of landing, as set by the user.
Written by Brian Diver comp 390_001
December 2023
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
exit_message = '''Execution complete'''


def run_meteorite_filter_from_user_input():
    """This method uses a Meteorite_Filter object to collect information from the user and output data"""
    filter = Meteorite_Filter()
    filter.get_input_from_user()
    filter.create_meteorite_list()
    filter.filter_meteorite_list()
    filter.output_meteorite_list()


print(welcome_message)
run_meteorite_filter_from_user_input()
print(exit_message)


