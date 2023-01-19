class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value >= 0:
            self.__x = value
        else:
            print('Координата должна быть > 0')

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value >= 0:
            self.__y = value
        else:
            print('Координата должна быть > 0')

    def __str__(self):
        return f'Point ({self.__x}, {self.__y})'


x, y = map(int, input().split())
point = Point()
point.x = x
point.y = y
print(point)

# point = Point()
# point.x = -1
# point.y = 3
# point.x = 5
# print(point)
# Координата должна быть > 0
# Point (5, 3)
