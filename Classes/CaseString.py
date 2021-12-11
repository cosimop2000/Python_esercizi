# Define a class named CaseString with the following methods:
#
# the constructor takes an initial string as a parameter
# set_upper: sets string mode (False = original case, True = upper case)
# set_string: sets the encapsulated string
# get_string: returns the string with the proper case


class CaseString:
    def __init__(self, s, upper_case=False):
        self.s = s
        self.upper_case = upper_case

    def set_string(self, s):
        self.s = s

    def set_case(self, upper_case):
        self.upper_case = upper_case

    def get_string(self):
        if self.upper_case:
            return self.s.upper()
        else:
            return self.s



