import random


# Write a program computing the sum of the first 100 integer numbers

def compute_100():
    sum = 0
    for i in range(101):
        sum = sum + i
    print(sum)


# Write a Python program to construct the following pattern, using a nested for loop.

def pattern():
    for j in range(10):
        for i in range(j):
            print('* ', end='')
        print()


# Write a program which can compute the factorial of a given number.

def factorial(x):
    if x < 0:
        return None
    elif x == 0:
        print(1)
    else:
        fact = x
        for i in range(x-1, 1, -1):
            fact *= i
        print(fact)


# Write a program to print the numbers divisible by 7 below 200.

def divisible_7_print():
    divisibles = []
    for i in range(1, 200):
        if i % 7 == 0:
            divisibles.append(i)
    print(divisibles)


# Write a program to show the Pitagoric table

def pitagoric_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j*i, '\t', end='')
        print()


# Write a Python program to simulate a dice game.
# There are 2 players, each player throws the dice, wins each game
# the player with the highest score. Wins the first one which reaches 1000 wins.

def dice_game(p1, p2):
    p1_wins = p2_wins = 0

    while p1_wins < 1000 and p2_wins < 1000:
        rand1 = random.randint(1, 6)
        rand2 = random.randint(1, 6)
        if rand1 > rand2:
            p1_wins += 1
        elif rand2 > rand1:
            p2_wins += 1

    print(p1, p1_wins, sep='-->')
    print(p2, p2_wins, sep='-->')


# write a program to compute the Fibonacci series until an arbitrary number.

def fibonacci(n):
    if n <= 0:
        return None

    sequence = [0, 1]
    while True:
        i = sequence[-1] + sequence[-2]
        if i > n:
            break
        sequence.append(i)

    print(sequence)


# Write a binary search function which
# searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

def binary_search(l, elem):
    l.sort()
    bottom = 0
    top = len(l) - 1
    index = -1
    while top >= bottom and index == -1:
        import math
        mid = int(math.floor((top + bottom) / 2.0))
        if l[mid] == elem:
            index = mid
        elif l[mid] > elem:
            top = mid - 1
        else:
            bottom = mid + 1

    print(index)
