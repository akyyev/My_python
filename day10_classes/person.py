import datetime
# from module_name import ClassName
from day10_classes.rocket import Rocket
from day06_OOP_concepts.practice02_inheritance import Bird
from math import sqrt as square_root

class Person:

    def __init__(self, name="N/A", date_of_birth="1-1-1995", POB="US", SSN="XXX-XX-1234"):
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = POB
        self.__SSN = SSN

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name}.")

    def static_method():
        print("This is static method")

    def get_age(self):
        today = datetime.date.today().year
        datetime_obj = datetime.datetime.strptime(self.date_of_birth, '%m-%d-%Y')

        return today - datetime_obj.year

    def __str__(self):
        return f"{self.name} is {self.get_age()} years old. POB: {self.place_of_birth} {self.__SSN}"


p1 = Person()
Person.static_method()
p1.introduce_yourself()
# print(p1.__SSN)
print(p1)


class Student(Person):
    def __init__(self, name, date_of_birth, POB, SSN, graduation_year, gpa):
        super().__init__(name, date_of_birth, POB, SSN)
        self.gpa = 0
        self.graduation_year = graduation_year
        self.set_gpa(gpa)

    def set_gpa(self, gpa):
        if gpa > 4.0 or gpa < 0.0:
            raise Exception("invalid gpa")
        else:
            self.gpa = gpa


s1 = Student("Tom", "2-4-2000", "Canada", "XXX", 2020, 3.5)
print(s1)
print(s1.graduation_year)
print(s1.gpa)
# after importing rocket class
# we can use it
print(Rocket(1, 2))
print(Bird("Asman").whoisThis())
print(square_root(10))
