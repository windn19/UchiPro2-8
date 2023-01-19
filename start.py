class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('Иван', 15)
print(person.name)
print(person.age)
person.age = 166
print(person.age)
