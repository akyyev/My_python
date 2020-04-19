items_in_cart = 3

try:
    if items_in_cart != 2:
        raise ValueError('Product count not matching')
except ValueError:
    print('error occurred')
finally:
    print('Final block always gets executed')

# assert (items_in_cart != 2)  # AssertionError


try:
    with open('test.txt', 'r') as reader:
        reader.read()
except FileNotFoundError as e:
    print('File not founded', e)
finally:
    print('Final block always gets executed no matter what')
