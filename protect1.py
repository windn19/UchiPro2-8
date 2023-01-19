class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport


person = Person('Иван', 15, 1234567890)
person._age = 116
print(person._age)
print(person._Person__passport)
