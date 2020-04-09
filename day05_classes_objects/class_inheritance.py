class Person:
    def move(self):
        print("Moves 4 paces")

    def rest(self):
        print("Gains 4 health points")


class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")


class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")

    def move(self):
        print("Moves 6 paces")


class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("Turns invisible")

    def heal(self):
        print("Heals 15 health points")


class Magic:
    def magic(self):
        print("Magic show 5 point damage")


character1 = Wizard()
character1.move()

character2 = Magic()
character2.magic()

