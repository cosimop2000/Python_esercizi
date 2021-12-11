# Define a class named Circle which can be constructed by a radius.
# The Circle class has two methods for computing perimeter and area, respectively
# Define a class named Rectangle which can be constructed by length and width.
# The Rectangle class has two methods for computing perimeter and area, respectively.
# Define a class named Shape and its subclass Square.
# The Square class has a constructor which takes a length as argument.
# Both classes have an area function which can print the area of the
# shape where Shape's area is 0 by default.
import math


class Shape:
    def __init__(self):
        pass

    def print_area(self):
        return 0

    def print_perimeter(self):
        return 0

    def get_name(self):
        return type(self)


class Square(Shape):
    def __init__(self, lenght):
        super().__init__()
        self.lenght = lenght

    def print_area(self):
        return self.lenght**2

    def print_perimeter(self):
        return self.lenght*4


class Rectangle(Shape):

    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def print_area(self):
        return self.base*self.altezza

    def print_perimeter(self):
        return 2*(self.base + self.altezza)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def print_area(self):
        return math.pi * (self.radius**2)

    def print_perimeter(self):
        return self.radius * 2 * math.pi
