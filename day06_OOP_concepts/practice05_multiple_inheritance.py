# Multiple Inheritance in Python
class Base1:

    def print_one(self):
        print("This is base1")


class Base2:
    def print_two(self):
        print("This is base2")


class MultiDerived(Base1, Base2):
    def print_derived(self):
        print("This is sub")


sub = MultiDerived()
sub.print_one()
sub.print_two()
sub.print_derived()
#  Method Resolution Order (MRO).
print(MultiDerived.__mro__)


# Multilevel Inheritance in Python
class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Derived1(Base):
    def __init__(self, name, age):
        super().__init__(name, age)


class Derived2(Derived1):
    def __init__(self):
        super().__init__("Bob", 10)


#  Method Resolution Order (MRO).
print(Derived2.__mro__)
der2 = Derived2()
print(der2.name)
print(der2.age)
