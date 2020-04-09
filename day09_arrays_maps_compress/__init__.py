# Read a 2D list of integers:

NUM_COLUMN = 5
NUM_ROWS = 3
a = [[0]*NUM_COLUMN]*NUM_ROWS

print(a)

NUM_ROWS = int(input().split()[0])

a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]

c = int(input())

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] *= c

print(a)
