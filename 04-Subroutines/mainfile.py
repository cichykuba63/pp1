from mymath import *

random_number = generate_number()
user_number = read_numbers()

if user_number == random_number:
    print("That's the number.")
else:
    print("That is not the number.")