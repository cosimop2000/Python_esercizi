# Define a class Person and two child classes: Male and Female.
# All classes have a method getGender which can print 'Male'
# for Male class and 'Female' for Female class.

class Person:
    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        return 'Male'


class Female(Person):
    def get_gender(self):
        return 'Female'
