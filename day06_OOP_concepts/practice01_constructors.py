import math


class ComplexNumber:
    name = "Complex Number"

    def __init__(self, a=0, b=0):
        self.real = a
        self.imaginary = b

    def getData(self):
        print(f"{self.real}+{self.imaginary}i")

    def get_distance(self, comp_num):
        return math.sqrt(math.pow(self.real - comp_num.real, 2) + math.pow(self.imaginary - comp_num.imaginary, 2))


c1 = ComplexNumber(4, 6)
c2 = ComplexNumber(1, 2)
c3 = ComplexNumber()

c1.getData()
c2.getData()
c3.getData()

print(c1.get_distance(c2))
print(c3.name)

ComplexNumber.name = "Imaginary"
print(c1.name)
print(c2.name)
print(c3.name)

# adding new attribute to specific object
c1.newAttribute = 10
c1.getData()
print(c1.newAttribute)

# c2 has no that attribute
# print(c2.newAttribute)


# adding new attribute to the class
ComplexNumber.formula = "a+bi"
print(c1.formula)
print(c2.formula)

del ComplexNumber.formula
# print(c2.formula)

print(type(c1))
print(isinstance(c1, ComplexNumber))
print(issubclass(bool, int))