# Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user.

print()
user_choice = int(input("Enter number: "))

for n in range(1, 11, 1):
    print(f"{user_choice} * {n} = {user_choice * n}")