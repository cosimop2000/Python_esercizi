# Write a function receiving a number and printing
# the square of that number if it is below 200. Otherwise, it returns 200.

def square(n):
    if n*n < 200:
        return n*n
    else:
        return n


# Write a Python program to compute the sum of first
# 100 squared integers using the while construct.

def compute_100():
    sum_ = n = 0
    while n < 100:
        sum_ = sum_ + n*n
        n = n + 1

    print(sum_)


# Write a Python program to compute all the multiples of 17
# below 300 using the while construct

def compute(n):
    numbers = []
    multiple = 0
    index = 1

    while multiple < 300:
        multiple = n * index
        if multiple < 300:
            index = index + 1
            numbers.append(multiple)

    print(numbers)


# Define a function that can accept two strings as input and print
# the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def get_longest(s1, s2):
    if len(s1) == len(s2):
        print(s1)
        print(s2)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)


# Define a function that can accept an integer number
# as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

def check_value(n):
    if isinstance(n, int):
        if n % 2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")

