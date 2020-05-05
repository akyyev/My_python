print("Hello World!")

for i in range(100):
    if i == 0:
        continue
    elif i % 15 == 0:
        print(str(i) + " = fizzbuzz")
    elif i % 5 == 0:
        print(str(i) + " = buzz")
    elif i % 3 == 0:
        print(str(i) + " = fizz")
    else:
        print(i)

class Rectangle(Shape):
   def __init__(self, length, breadth, unit_cost=0):
      self.length = length
      self.breadth = breadth
      self.unit_cost = unit_cost

   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
      area = self.get_area()
      return area * self.unit_cost



class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

print()
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle: %s cm^2" % (r.get_area()))
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost()))



