class Person:
    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        super().__setattr__('passport', passport)

    def __setattr__(self, key, value):
        if key == 'name' or key == 'age':
            super().__setattr__(key, value)
        else:
            print('Нет доступа')


person = Person('Иван', 15, 1234567890)
person.name = 'Иван Иванов'
person.passport = 1111111111
print(person.name, person.passport)
