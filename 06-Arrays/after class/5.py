# An array contains values: 15, 8, 31, 47, 2, 19. 
# Create a program that calculates and displays the array and the arithmetic mean of array values. 
# Use the “for” loop statement.

arr = [15, 8, 31, 47, 2, 19]
z = 0

for n in arr:
    if n == arr[0]:
        print("Array: ", end = "")
    print(n, end = " ")

for n in arr:
    z += n

z = z / len(arr)

print(f"\nArithmetic mean: {round(z, 2)}")
