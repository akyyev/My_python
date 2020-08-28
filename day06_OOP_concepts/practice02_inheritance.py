class Bird:
    def __init__(self, name):
        print("{} is ready".format(name))

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

    def method(self):
        print('This is method in Bird class')


class Animal:
    def __init__(self, name):
        print("{} is ready".format(name))

    def whoisThis(self):
        print('Animal')

    def method(self):
        print('This is method in Animal class')


# child class
class Penguin(Animal, Bird):

    def __init__(self):
        # call super() function
        super().__init__("Penguin")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


lemon = Bird("Lemon")
lemon.whoisThis()

peggy = Penguin()
peggy.whoisThis()
peggy.method() # inheritance occurs according to order of super classes
# peggy.swim()
# peggy.run()
