# Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. Entering 0 ends entering numbers.

user_choice = -1
x = 0
y = 0
z = 0

while user_choice != 0:
    user_choice = int(input("Enter number: "))

    if user_choice != 0:
        x += 1
        
    y += user_choice
    z = y / x

print(f"RESULT: Quantity = {x}, Sum = {y}, Mean = {round(z, 2)}") 




