class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def change_age(self):
        self.__age += 1

    def rename(self, newname):
        self.__name = newname

    def get_info(self):
        return f'Имя: {self.__name}, возраст: {self.__age}'


person = Person('Иван', 15)
person.change_age()
print(person.get_info())
print(person.__age)
# print(person.age)
# person.age = 166
# print(person.age)
