class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport


person = Person('Иван', 15, 1234567890)
print(person.name)
print(person._age)
print(person.__passport)
        