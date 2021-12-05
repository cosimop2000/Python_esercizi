import MyString


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


if __name__ == '__main__':
    print_hi('Cosimo')
    print_hi("Inter")
    print_prova()
    print('Hello world')

    # String basics exercises
    mystring_function()
