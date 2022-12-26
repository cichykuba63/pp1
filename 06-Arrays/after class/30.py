# A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last column. 
# Display array values in rows and columns before and after changes

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 2], [6, 7, 9]]

print("Before changes: ", end = "")
for element in arr:
    print()
    for argument in element:
        print(argument, end = " ")
    
print("\n\nAfter changes: ", end = "")
for element in arr:
    element.insert(0, element[2])
    element.pop(3)
    element.insert(3, element[1])
    element.pop(1)

for element in arr:
    print()
    for argument in element:
        print(argument, end = " ")