import MyString


def print_hi(name):

    print(f'Hi, {name}')


def print_prova():

    print("Iron Maiden" + ' : Run to the hills')


def mystring_function():
    ciao = MyString
    MyString.ciaozzz()

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


if __name__ == '__main__':
    print_hi('Cosimo')
    print_hi("Inter")
    print_prova()
    print('Hello world')

    # String basics exercises
    mystring_function()
