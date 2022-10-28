# Define a function that displays integer numbers from 1 to N. Then call the function and display numbers from 1 to 15.

def numbers(x):
    for i in range(1, x+1):
        print(i, end = " ")

numbers(20)
print()
numbers(25)