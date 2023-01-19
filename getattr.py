class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.passport = passport

    def __getattribute__(self, item):
        if item == 'passport':
            return 'Нет доступа'
        return super().__getattribute__(item)


person = Person('Иван', 15, 1234567890)
print(person.name)
print(person.passport)
