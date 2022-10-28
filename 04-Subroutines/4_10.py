# Define a function read_number() that returns an integer number entered from the keyboard. 
# The function should print a text prompting user to enter the number 'Enter a number: '. 
# Then use the function to read two numbers from the keyboard. Display their sum.

def read_number():
    global user_choice1
    global user_choice2
    user_choice1 = int(input("Enter the first number: "))
    user_choice2 = int(input("Enter the second number: "))

def sum():
    print(f"{user_choice1} + {user_choice2} = {user_choice1 + user_choice2}")

read_number()
sum()


    