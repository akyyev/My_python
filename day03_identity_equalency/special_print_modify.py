

def greeting(name, age=28):
    print("Hello " + name.capitalize() + ", you are " + str(age) + "!")
    print(f"Hello {name.capitalize()}, you are {age}!")


name = input("Enter your name: ")
greeting(name, 32)
greeting("Judith")
