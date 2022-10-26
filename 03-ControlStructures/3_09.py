# A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

user_choice1 = int(input("Insert the first number: "))
user_choice2 = int(input("Insert the second number: "))

if user_choice1 > 0 and user_choice2 > 0:
    print("Both are positive")
elif user_choice1 > 0 or user_choice2 > 0:
    print("One of them is positive")
else:
    print("None of them is positive")