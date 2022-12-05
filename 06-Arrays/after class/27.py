# An array contains values: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
# Create a program that modifies the array values to create a multiplication table as below. 
# Use loop statements. Display the array.
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n = 0

for i in range(0, 5):
    n += 1
    arr[0][i] += n

n = 0

for i in range(0, 5):
    n += 2
    arr[1][i] += n

n = 0

for i in range(0, 5):
    n += 3
    arr[2][i] += n

n = 0

for i in range(0, 5):
    n += 4
    arr[3][i] += n

n = 0

for i in range(0, 5):
    n += 5
    arr[4][i] += n

for a in arr:
    for e in a:
        print(e, end = " ")
    print()


