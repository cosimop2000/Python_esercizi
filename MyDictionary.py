# function which can generate an example
# dictionary containing 5 key, value couples.
# Specifically, the keys represent phone numbers, and the values represent names.

def get_dict():
    diz = dict()
    diz.update({'123': 'Cos', '3472345678': 'Filippo Bolognesi',
                '3475654564': 'Chiara Lazzari', '3478796656': 'Luca Boldrini',
                '3477738394': 'Andrea Pluglisi', '3471232123': 'Roberta Pasolini'})
    print(diz)


# function which can generate an example dictionary representing a person. Keys must be: name, surname, address, age.

def get_dict_v2(keys, values):
    if len(keys) != len(values):
        return None
    diz = {}
    for i in range(0, len(keys)):
        diz[keys[i]] = values[i]
    print(diz)


# function which can generate a dictionary where the keys are numbers between 1 and 20
# (both included) and the values are square of keys.
# The function should return the dictionary itself.
# Then, calculate the average of both keys and values.

def gen_dict_v3(n):
    diz = {}

    for i in range(1, n+1):
        diz[i] = i**2
    print(diz)
    keys_mezzi = 0
    values_mezzi = 0
    print(sum(diz.keys()) / len(diz), sum(diz.values()) / len(diz), sep='->')
    return diz, keys_mezzi, values_mezzi


# program which count and print the numbers of each character in a string.

def count(s):
    diz = {}
    for c in s:
        if c in diz:
            diz[c] += 1
        else:
            diz[c] = 1
    print(diz)


# program that accepts a string and calculate the number of letters and digits

def calculate(s):
    diz = {'letters': 0, 'digits': 0}
    for c in s:
        if c.isalpha():
            diz['letters'] += 1
        elif c.isnumeric():
            diz['digits'] += 1
    print(diz)
