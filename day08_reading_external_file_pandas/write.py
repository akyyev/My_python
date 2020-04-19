# file = open('test.txt')
# file.close()
# is not necessary when using --> with open('test.txt','r') as file:
# and it's more preferable
# r for read mode
# w for write mode

# Task:
# read the file and store all the lines in list
# reverse the list
# write back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    print(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)