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

def compose_string(strx):
    if len(strx) < 2:
        return ''
    else:
        s = strx[0:2] + strx[-2:]
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


# Write a Python function to reverses a string if its length is a multiple of 4.
# Otherwise, it returns the original string

def reverse(s):
    if (len(s) % 4) == 0:
        return s[::-1]
    else:
        return s


# Write a program which accepts a string as input and
# print 'Yes' if the string is 'yes' in any case form
# (e.g., Yes, YES, yes, yEs...), otherwise print "No"

def normalize(s):
    if s.upper() == 'YES':
        print("Yes")
    else:
        print('No')


# Please write a program which accepts
# a string from console and print the characters that have even indexes.
# Remember slicing supports increments!

def even_index(s):
    if s is not None:
        return s[::2]


# Write a Python program to add 'ing' at the end of a given string.
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.

def concat_ing(s):
    if len(s) < 3:
        return s
    elif s[-3:] == 'ing':
        return '{}ly'.format(s)
    else:
        return '{}ing'.format(s)


# Write a Python function to return a string made of
# 4 copies of the last two characters of a specified string (length must be at least 2)

def four_copies(s):
    if len(s) >= 2:
        return s[-2:] * 4


# Write a program to split a string on the last occurrence of the delimiter.
# See the str.rsplit()

def split_delimitate(s, delimitator):
    if delimitator in s:
        return s.rsplit(',', 1)
