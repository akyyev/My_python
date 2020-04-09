class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, num):
        self.y += num

    def move(self, x_inc=0, y_inc=0):
        self.x += x_inc
        self.y += y_inc

    def land_rocket(self):
        self.x = 0
        self.y = 0

    def safety_check(self, other):
        dist = self.get_distance(other)
        if dist == 0:
            print("You have crashed to another rocket!")
        elif dist < 4:
            print("You are so close to another rocket!")
        else:
            print("You are safe!")

    def get_distance(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** .5
        return distance

    # to compare to rockets with ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Point: " + str(self.x) + " " + str(self.y)


r1 = Rocket()
r2 = Rocket()
r3 = r1
print(r1)
print(r1 == r2)
print(r1 is r2)
print(r3 is r1)

r1.move_up(10)
# multiple rockets
ls = []

for i in range(5):
    ls.append(Rocket(i))

ls[0].move(y_inc=400)
ls[1].move(100)

for index, rocket in enumerate(ls):
    print("Rocket %d is at (%d, %d)" % (index, rocket.x, rocket.y))

r4 = Rocket(1, 2)
r5 = Rocket(4, 6)

dist = r4.get_distance(r5)
print("The rockets are %0.01f units apart" % dist)


class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


shuttle = Shuttle(10, 0, 3)
print(shuttle)
