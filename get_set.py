class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport

    def get_passport(self):
        return self.__passport

    def set_passport(self, passport):
        if isinstance(passport, int) and len(str(passport)) == 10:
            self.__passport = passport
        else:
            print('Неверный номер паспорта')


person = Person('Иван', 15, 1234567890)
person.set_passport(111111111)
print(person.get_passport())
