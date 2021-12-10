import MyIterative
import MyString
import MyConditionalStatement


def print_hi(name):

    print(f'Hi, {name}')


def print_prova():

    print("Iron Maiden" + ' : Run to the hills')


def mystring_function():
    ciao = MyString
    MyString.ciaozzz()

    print("\n Esercizi sulle stringhe \n")

    print(ciao.converter_int_string(123))

    ciao.concatenate("Banana", "fish")

    ciao.replace_instances("'I like cats and dogs, but I'd much rather own a dog.'")

    print(ciao.compose_string('Cosimo'))
    print(ciao.compose_string('w3'))
    print(ciao.compose_string('X'))

    ciao.replace_all("cosimo ccccc Cosimo")

    ciao.zip_string('Cod', 'Fifa')
    ciao.zip_string('xxx', 'zzz')

    print(ciao.remove_char("cacca", 10))
    print(ciao.remove_char("cacca", 3))

    print(ciao.test_password("caddddd"))
    print(ciao.test_password("cad"))
    print(ciao.test_password("cadddddZZZZZZZZZZZZ"))
    print(ciao.test_password("12345678"))
    print(ciao.test_password("cad345ddd"))

    print(ciao.reverse("Dio"))
    print(ciao.reverse('abcdefgh    '))

    ciao.normalize('banana')
    ciao.normalize("yEs")

    print(ciao.even_index('banana'))
    print(ciao.even_index('H1e2l3l4o5w6o7r8l9d'))

    print(ciao.concat_ing('banana'))
    print(ciao.concat_ing('Os'))
    print(ciao.concat_ing('reading'))

    print(ciao.four_copies("banana"))

    print(ciao.split_delimitate("ciao,  scemo   , ffffff, ,   campana , medusa", ','))


def myconditional_function():
    stat = MyConditionalStatement

    print("\n Esercizi  \n")

    print(stat.square(11))

    stat.compute_100()

    stat.compute(17)

    stat.get_longest('ciao', 'ciao')
    stat.get_longest('banana', 'fish')

    stat.check_value(100.122)
    stat.check_value(101)


def myiterative_function():
    print("\n Esercizi  \n")
    sss = MyIterative

    sss.compute_100()
    sss.pattern()
    sss.factorial(5)
    sss.divisible_7_print()
    sss.pitagoric_table(10)
    sss.dice_game('Cosimo', 'Luca')
    sss.fibonacci(25)
    sss.binary_search(list(range(1, 100, 3)), 11)
    sss.binary_search([10, 32, 25, 3, 333, 9], 333)


def mylist_function():
    print("\n Esercizi  \n")
    import MyList
    lll = MyList
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lll.divide(li)
    lll.divide([1, 2, 3, 4, 5, 6, 7, 8, 9])
    lll.duplicate(li)
    lll.gen_list(20)
    lll.gen_list1(200, 300)
    lll.sort_list('banana,apple,strawberry,cherry,pineapple')
    lll.longer_than(['banana', 'apple', 'strawberry', 'cherry', 'pineapple'], 8)
    lll.remove_duplicates([1, 1, 1, 11, 111, 2, 3456, '1', 1.9, 1])
    lll.contains_duplicate([1, 2], [1, 5])
    lll.multiply_list([1, 2, 3, 4], [2, 3, 4, 5])

if __name__ == '__main__':
    print_hi('Cosimo')
    print_hi("Inter")
    print_prova()
    print('Hello world')

    # String basics exercises
    mystring_function()

    # Conditional exercises
    myconditional_function()

    myiterative_function()

    mylist_function()