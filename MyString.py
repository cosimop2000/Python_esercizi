def ciaozzz():
    print("gog")


# Define a function that can convert a integer into a string.


def converter_int_string(n):
    return str(n)


# Write a program to concatenate two strings using the .format() method.

def concatenate(s1, s2):
    print('{} {} '.format(s1, s2))


# Write a program to replace all instances of 'dog' with 'bird' in
# the following sentence: 'I like cats and dogs, but I'd much rather own a dog.'

def replace_instances(s):
    message = s
    print(message.replace('dog', 'bird'))


# Write a Python function to compose a string
# made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.

def compose_string(str):
    if len(str) < 2:
        return ''
    else:
        s = str[0:2] + str[-2:]
        return s


# Write a Python program that, given a string,
# replaces all occurrences of its first char with '$', except the first char itself.

def replace_all(s):
    first = s[0]
    print(first + s[1:].replace(first, '$'))


# Write a Python program to produce a single string
# given two strings as per below. Use slicing combined with the str.format() method()

def zip_string(s1, s2):
    if len(s1) == len(s2):
        print('{}{}  {}{}'.format(s1[0:-1], s2[-1], s2[0:-1], s1[-1]))


# Write a Python program to remove the nth index character from a nonempty string.

def remove_char(s, index):
    if s and len(s) > index + 1:
        return s[:index] + s[index+1:]
    else:
        return s


# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# The password have to be composed of only numbers or only digits

def test_password(password):
    if 6 <= len(password) <= 12:
        if password.isnumeric() or password.isalpha():
            return True
        else:
            return False
    else:
        return False

