# Write a program that calculates a dog's age in dog’s years. 
# For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years.

user_data = int(input("Enter the dog's age in human years: "))

if user_data <= 2:
    print(f"The dog's age in dog's years is {user_data * 10.5} years.")
elif user_data > 2:
    print(f"The dog's age in dog's years is {int((2 * 10.5) + ((user_data - 2) * 4))} years.")
