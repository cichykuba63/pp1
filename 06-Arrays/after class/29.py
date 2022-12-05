# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last row. 
# Display array values in rows and columns before and after changes.

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 5], [6, 3, 9]]

print("Before changes: \n", end = "")
for a in arr:
    for number in a:
        print(number, end = " ")
    print()

arr.insert(0, arr[4])
arr.pop(5)
arr.insert(len(arr), arr[1])
arr.pop(1)

print("After changes: \n", end = "")
for a in arr:
    for number in a:
        print(number, end = " ")
    print()