# The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b.

a = 5
b = 20

print("*" * b)

for element in range(0, a, 1):
    print("*", " " * (b - 4), "*")

print("*" * b)

