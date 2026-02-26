class Person:
    def __init__(self, name, age):
        self.name = name          # public
        self.__age = age          # private

    def get_age(self):
        return self.__age