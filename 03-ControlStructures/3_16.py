# Write a program that displays two numbers entered from the keyboard in ascending order.

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

if number_one > number_two:
    print(f"The higher number is {number_one}\nThe lower number is {number_two}")
elif number_two > number_one:
    print(f"The higher number is {number_two}\nThe lower number is {number_one}")
elif number_one == number_two:
    print(f"Number one {number_one} is equal to number two {number_two}")
else:
    print("Something went wrong.")