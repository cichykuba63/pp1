# A two-dimensional array contains the following numbers:
# 7 3 7 9 0
# 2 9 0 1 5
# 3 8 6 4 7
# 8 7 1 1 5
# Create a program that calculates the sum of values in the last column.

arr = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]
x = 0

for element in arr[3]:
    x += element

print(f"Sum of the last row: {x}")