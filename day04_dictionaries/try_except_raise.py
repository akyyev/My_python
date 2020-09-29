print("Errors: Try/Except")

# try:
#       code you want to run
# except:
#       executed if error occurs
# else:
#       executed if no error
# finally:
#       always executed


try:
    num = int(input('Enter a number between 1 and 30: '))
    num1 = 30 / num
    if not 1 < num < 30:
        raise ValueError(num)
except ValueError as err:
    print(err, num, "Bad Value! Value needs to be between 1 and 30!")
except ZeroDivisionError as err:
    print(err, ": Dividing with 0 is not allowed")
except:
    print("invalid input!")
else:
    print(f"30 divided by {num}, is:  {30 / num}")
finally:
    print("**Thank you for playing!**")
