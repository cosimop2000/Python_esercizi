# Given a list write a program to print the first half values in one line
# and the last half values in a single line line.
import itertools
import random


def divide(li):
    x = len(li)
    x /= 2
    print(li[:int(x)], li[int(x):])


# Write a program that, given a list,
# produces another list containing all the original values multiplied by 2.

def duplicate(li):
    new = []
    for i in li:
        new.append(i*2)
    print(new)


# generate a list where the values are square of numbers between 1 and 20
# (both included). Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values

def gen_list(n):
    new = []
    for i in range(1, n+1):
        new.append(i**2)
    print(new)


# find all numbers which are divisible by 7 but are not a multiple of 5,
# between 200 and 300 (both included). The numbers obtained should be
# printed in a comma-separated sequence on a single line.
# Consider the use of str.join() for joining the elements of a list.
# accepts a sequence of comma-separated numbers and generate a list which contains every element

def gen_list1(a, b):
    new = []
    for i in range(a, b+1):
        if i % 7 == 0 and i % 5 != 0:
            new.append(str(i))
    s = ','.join(new)
    print(s)
    print(s.split(','))


# accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting them alphabetically.

def sort_list(words):
    if ',' in words:
        print(','.join(sorted(words.split(','), reverse=True)))


# function to return, given a list of words, all the words that are longer than min_lenght

def longer_than(words, min_lenght):
    new = []
    for i in words:
        if len(i) > min_lenght:
            new.append(i)
    print(new)


# function to remove duplicates from a list without using sets.

def remove_duplicates(li):
    unique = []
    for i in li:
        if i in unique:
            continue
        unique.append(i)
    print(unique)


# function that takes two lists and returns True if they have at least one common member

def contains_duplicate(li1, li2):
    x = False
    for i in li1:
        if i in li2:
            x = True
    else:
        print(x)


# function to iterate over two lists simultaneously.
# Given two lists, the function checks if they have the same length
# and returns a list containing the product of corresponding elements

def multiply_list(li1, li2):
    if len(li1) != len(li2):
        return None
    new = []
    for i in range(0, len(li2)):
        new.append(li1[i] * li2[i])
    print(new)


# sort,sorting, shuffle

def try_basic(li):
    print(li)
    print(sorted(li, reverse=True))
    li.sort()
    random.shuffle(li)
    print(li)


# program which prints all permutations of [1,2,3]. Use itertools.permutations() to get permutations of list.

def permute(li):
    print(list(itertools.permutations(li)))


# generate a list with 5 random numbers between 100 and 200 inclusive. Use random.sample()

def gen_list2():
    x = random.sample(range(100, 201), 5)
    print(list(x))