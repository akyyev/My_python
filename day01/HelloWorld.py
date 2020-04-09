print("Hello World")

num1 = 0.0037 / 100
num2 = 0.000037

# even though numbers are equal it prints false, because of float numbers binary conversion
print(num1 == num2)

if round(num1, 4) == round(num2, 4):
    print("Equal")
    print(round(num2, 5))
else:
    print("No equal")

print(round(12.3453))

x = 0
while x < 20:
    x += 2
    print(x)

