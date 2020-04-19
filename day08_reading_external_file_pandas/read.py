file = open('test.txt')

# read n number of characters by passing parameter
# print(file.read(10))

# to read just one line
# print(file.readline())
# print(file.readline())


# Print line by line using readLine method
for i in file.readlines():
    # black line is added by default of print method so to remove black line use end = ''
    print(i, end='')

# line = file.readline()
# while line is not '':
#     print(line, end='')
#     line = file.readline()


file.close()
