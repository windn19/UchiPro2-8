class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_age(self):
        self.age += 1

    def rename(self, newname):
        self.name = newname

    def get_info(self):
        return f'Имя: {self.name}, возраст: {self.age}'


person = Person('Иван', 15)
person.change_age()
print(person.age)
person.age = 166
print(person.age)
