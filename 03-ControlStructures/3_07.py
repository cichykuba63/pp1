# X contains any integer value. Write a program to check that the value is even

number = int(input("Insert your x number: "))
division = number % 2

if division == 0:
    print("Your number is even")
else:
    print("Your number is odd")
