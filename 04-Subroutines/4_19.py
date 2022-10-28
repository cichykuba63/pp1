# Define a function that checks if the number is within the given range <x, y>. The function returns boolean value. 
# Then create a program and use the function you defined

def checking(n, x, y):
    global z
    for i in range(x, y+1):
        if n == i:
            z = True
            break
        else:
            z = False
    return x

user_choice1 = int(input("Enter the number you want to search: "))
user_choice2 = int(input("Enter the number opening searching: "))
user_choice3 = int(input("Enter the number shutting searching: "))

y = checking(user_choice1, user_choice2, user_choice3)

if z == True:
    print("That value is inside indicated numbers")
else:
    print("That value is outside the indicated numbers")

