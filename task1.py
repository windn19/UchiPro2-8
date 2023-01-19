class Student:
    def __init__(self, name, course):
        self.name = name
        self.__course = course
        self.__status = 'student'

    def next_course(self):
        if self.__course < 11:
            self.__course += 1
        else:
            self.__status = 'graduate'
            self.__course = None

    def deduction(self):
        self.__course = None
        self.__status = 'expelled'

    def get_info(self):
        return f'Student: {self.name} ({self.__course}), status: {self.__status}'


# student1 = Student('Михайлов Петр', 10)
# print(student1.get_info())
# student1.next_course()
# student1.next_course()
# print(student1.get_info())
#
# student2 = Student('Васильев Сергей', 5)
# print(student2.get_info())
# student2.deduction()
# print(student2.get_info())

name = input('Введите ФИО: ')
course = int(input('Введите класс: '))
command = input('Введите команду: ')
student = Student(name, course)
if hasattr(student, command):
    getattr(student, command)()
    print(student.get_info())
else:
    print('Неизвестная команда')
