import datetime


class Car:
    def __init__(self, make, model, year=2010, mileage=20000):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"This is {self.make} {self.model}, year - {self.year}"

    def worth_to_buy(self):
        year = datetime.date.today().year

        mileage = (year - self.year) * 5000
        if self.mileage < mileage / 2:
            print("Definitely worth it")
        elif self.mileage < mileage:
            print("Good deal")
        else:
            print("Not worth to buy")


c1 = Car("Toyota", "Camry", 2015, 10000)
print(c1.mileage)
c1.worth_to_buy()
