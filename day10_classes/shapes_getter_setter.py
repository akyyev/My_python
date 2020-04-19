class Shape:
    name = 'Shape'

    def __init__(self):
        pass

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, height):
        super().__init__()
        self.__length = length
        self.__height = height
        self._age = 0

    def area(self):
        return self.__length * self.__height

    # decorators come together @property tag with
    # method name as 'm1' and @m1.setter tag
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, x):
        self.__length = x

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if val < 0:
            self.__height = 0
            raise ValueError
        else:
            self.__height = val


r = Rectangle(3, 4)
r.length = 2
r.height = 5
print(r.area())
print(r.length)
