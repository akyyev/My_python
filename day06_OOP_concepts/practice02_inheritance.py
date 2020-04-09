class Bird:
    def __init__(self, name):
        print("{} is ready".format(name))

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

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
# peggy.swim()
# peggy.run()

