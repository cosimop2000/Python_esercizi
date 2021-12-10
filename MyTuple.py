# program to get the 4th element and 4th element from the end of a given tuple (length must be at least 6).

def f_a(tup):
    if len(tup) > 6:
        print(tup[4-1], tup[-4])


# check whether an element exists within a tuple.

def check(tup, elem):
    if elem in tup:
        print(True)


# convert a list to a tuple.

def convert(li):
    new = tuple(li)
    print(new)


# function to remove an item with index n from a tuple.

def remove_item(tup, index):
    x = list(tup)
    x.pop(index)
    x = tuple(x)
    print(x)
    return x


# function to double the last value of each tuple in a list.

def double_last(li):
    new = []
    for t in li:
        new.append((t[0], t[1], t[2] * 2))
    print(new)
    return new


# write a program to generate all sentences where subject is in
# ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

def generate_sentence(subjects, verbs, objects):
    for i in range(len(subjects)):
        for j in range(len(verbs)):
            for k in range(len(objects)):
                sentence = '{} {} {} '.format(subjects[i], verbs[j], objects[k])
                print(sentence)


# program for sorting a list of tuples (each tuple has 3 elements) according with the 2nd element of each tuple.
# program for sorting a list of tuples (each tuple has 2 elements) according with the product of the
# two elements of each tuple.
#  program for sorting a list of strings according with the 3rd letter of each string (descending order).

def sort_tup(li1, li2, li3):
    x = sorted(li1, key=lambda i: i[1])
    print(x)

    y = sorted(li2, key=lambda t: t[0] * t[1])
    print(y)

    z = sorted(li3, key=lambda s: s[2], reverse=True)
    print(z)


# Sort the (name, age, height) tuples by ascending order where name is string, age
# and height are numbers. Sort by height, name, age in this order.

def sort_multilevel(li):
    from operator import itemgetter
    x = sorted(li, key=itemgetter(2, 0, 1), reverse=True)
    print(x)
