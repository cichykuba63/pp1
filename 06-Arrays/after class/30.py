# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Display array values in rows and columns before and after changes

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 3, 5], [6, 3, 9]]

print("Before changes: \n", end = "")
for a in arr:
    for number in a:
        print(number, end = " ")
    print()

for a in arr:
    a.insert(0, a[len(a) - 1])
    a.pop(len(a) - 1)
    a.insert(len(a), a[1])
    a.pop(1)

print("After changes: \n", end = "")
for a in arr:
    for number in a:
        print(number, end = " ")
    print()
    