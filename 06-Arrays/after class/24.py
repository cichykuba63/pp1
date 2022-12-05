# A two-dimensional array of size 2 by 4 contains integer numbers. 
# Create a program that displays array values in rows and columns.

arr = [[1,2], [3,4], [5,6], [7,8]]

for r in arr:
    for v in r:
        print(v, end = " ")
    print()