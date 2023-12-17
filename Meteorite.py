"""This module defines the meteorite object that is used within many functions of Meteorite_Filter to contain data on
individual meteorites"""
from utility_functions import *


class Meteorite:
    """Every meteorite object has variables for the 12 pieces of data that come in the meteorite_landings.txt file.
    By looping through a complete list of meteorite objects, all these variables can be read by the Meteorite_Filter
    class"""
    def __init__(self):
        """All 12 variables are initialized to None when a meteorite object is created prior to setting any actual
        values. An attribute list is also created containing these variables so that all attributes can be collected
        in a single list to make looping possible. This method is more than 10 lines long, however the variables
        need to be initialized"""
        self.fall = None
        self.year = None
        self.rec_lat = None
        self.rec_long = None
        self.geo_location = None
        self.states = None
        self.mass = None
        self.rec_class = None
        self.name_type = None
        self.id = None
        self.name = None
        self.counties = None
        self.attribute_list = [self.name, self.id, self.name_type, self.rec_class, self.mass, self.fall, self.year,
                               self.rec_lat, self.rec_long, self.geo_location, self.states, self.counties]

    def set_meteorite_from_string(self, meteorite_as_string):
        """The original text file containing the meteorite data gives every meteorite as a separate string. This method
        turns that string into data for each individual variable to instantiate a meteorite object. The string is split
         on tab characters to create a list of 12 strings. That list is then used to set values for all meteorite
         variables using set_attributes_from_list()"""
        clean_meteorite_data = clean_data_list(meteorite_as_string)
        index = 0
        for attribute in clean_meteorite_data:
            self.attribute_list[index] = attribute
            index = index + 1
        self.set_attributes_from_list()

    def set_attributes_from_list(self):
        """This method uses the filled attribute list from set_meteorite_from_string() to set values for all variables
        in the meteorite object"""
        self.name = self.attribute_list[0]
        self.id = self.attribute_list[1]
        self.name_type = self.attribute_list[2]
        self.rec_class = self.attribute_list[3]
        self.set_mass(self.attribute_list[4])
        self.fall = self.attribute_list[5]
        self.set_year(self.attribute_list[6])
        self.rec_lat = self.attribute_list[7]
        self.rec_long = self.attribute_list[8]
        self.geo_location = self.attribute_list[9]
        self.states = self.attribute_list[10]
        self.counties = self.attribute_list[11]

    def set_mass(self, mass_input):
        """Unlike most other variables in this class that remain as a string, mass must be represented as a float for
        computational purposes. Some meteorites have no data for certain variables and a variable of type None can not
        be turned into a float. This method assures that no math is attempted when mass == None"""
        if mass_input is None:
            self.mass = None
        else:
            self.mass = float(mass_input)

    def set_year(self, year_input):
        """similar to mass, year must be an integer value to act as a filtering parameter. None can not be converted
        into an int and this method prevents that"""
        if year_input is None:
            self.year = None
        else:
            self.year = int(year_input)
