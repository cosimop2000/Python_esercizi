# class named American which has a static method called get_nationality.
# Use the @staticmethod decorator.

class American:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_nationality():
        return print('USA')

    def __repr__(self) -> str:
        return 'USA'


class NewYorker(American):
    pass
