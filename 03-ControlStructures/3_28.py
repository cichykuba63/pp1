# Write a program that displays the first fifty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, 
# each subsequent term is the sum of the previous two.

x = 0
y = 1

for i in range(1, 51, 1):
    z = x + y

    if i == 1:
        print("0", end = " ")
    elif i == 2:
        print("1", end = " ")

    if i > 2:
        print(z, end = " ")
        x = y
        y = z
