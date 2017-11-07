#pylint: disable=missing-docstring

import math

from datetime import datetime

# Function definitions

def hello(name):
    print("Hello my name is {}".format(name))

def count_up(start):

    return start, start+1, start+2

def convert_dob(dob_str):
    """Assumes DOB in the form YYYY/MM/DD"""

    dob = datetime.strptime(dob_str, "%Y/%m/%d")

    return dob

####

# Classes

class Person(object):

    def __init__(self, name, dob):
        self.name = name
        self.dob = convert_dob(dob)

    def say_hello(self):
        hello(self.name)

    def calc_age(self):

        age = datetime.now() - self.dob

        return math.floor(age.days / 365)
