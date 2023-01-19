class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self._age = age
        self.__passport = passport

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if isinstance(passport, int) and len(str(passport)) == 10:
            self.__passport = passport
        else:
            print('Неверный номер паспорта')


person = Person('Иван', 15, 1234567890)
person.passport = 123450
print(person.passport)
person.passport = 1111111111
print(person.passport)
