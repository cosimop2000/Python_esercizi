#  list comprehension to filter odd numbers in a list.

def filter_odd(n):
    li = [i for i in range(n) if i % 2 != 0]
    print(li)


# program to generate a list whose values are
# the first 50 even numbers. Then, transform the list into a tuple using tuple().

def filter_even(n):
    li = [i for i in range(n) if i % 2 == 0]
    print(tuple(li))


# program to get a list of strings and create a list of integers.
# Each integer represent the length of each initial string.

def len_str(li):
    new = [len(s) for s in li]
    for j in range(len(li)):
        print(li[j], new[j], sep='->', end='')
    print()


# program to output a random number, which is divisible by 5 and 7,
# between 0 and 200 inclusive using random module and list comprehension.
# Use random.choice() to a random element from a list.

def choice(n):
    import random
    li = [i for i in range(n+1) if i % 5 == 0 and i % 7 == 0]
    print(li, ' --> ', random.choice(li))


# program to print a given list after removing numbers which are divisible by 5 and 7

def remove_5_7(li):
    new = [i for i in li if i % 5 == 0 and i % 7 == 0]
    list_difference = [el for el in li if el not in new]
    print(list_difference)


# program that accepts a sequence of white space separated words as
# input and prints the words after removing all duplicate words and sorting them alphanumerically

def remove_duplicates(seq):
    new = seq.split(' ')
    s = ' '.join(sorted(set(new)))
    print(s)


# es

def f_a(s):
    new = [len(word) for word in s.split(' ') if word != 'the']
    print(new)


# program to print the list after removing the 0th, 2nd, 4th, 6th numbers
# delete a bunch of element from a list. Use enumerate() to get (index, value) tuple

def remove_el(li):
    if len(li) < 6:
        raise RuntimeError("Something is wrong")
    old = [(index, value) for (index, value) in enumerate(li)]
    new = [(index, value) for (index, value) in enumerate(li) if index % 2 != 0]
    print(old, new, sep='------->')
