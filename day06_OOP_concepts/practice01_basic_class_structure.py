class ClassWithEmptyBody:
    """This is a docstring. I have created empty class"""
    pass


# __doc__ gives us docstring of the class
print(ClassWithEmptyBody.__doc__)


class Parrot:
    # class attribute
    species = 'bird'
    count = 0

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Parrot.count += 1

    # instance methods
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate objects
sky = Parrot("Sky", 10)
lemon = Parrot("Lemon", 9)

# access the class attributes
print(f"Sky is a {sky.species}")
print(f"Lemon is a {lemon.species}")

# access the instance attributes
print("{} is {} years old".format(sky.name, sky.age))
print("{} is {} years old".format(lemon.name, lemon.age))
print(f"Two birds ({sky.name} and {lemon.name}) plays together")

print(sky.sing("'Happy'"))
print(sky.dance())

# Let's see how many object we've created
print(Parrot.count)


class MyClass:
    """This is my second class"""
    a = 10

    def func(self):
        print('Hello')

    def __greeting_private(self):
        print("Privately greetings!!!")

    def greeting(self):
        self.__greeting_private()
        print("Normal greetings!!!")


# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

# object
obj = MyClass()
obj.func()
# AttributeError: 'MyClass' object has no attribute '__greeting_private'
# obj.__greeting_private()
obj.greeting()
