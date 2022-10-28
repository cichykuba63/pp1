import random

def read_numbers():
    user_choice = int(input("Enter your number: "))
    return user_choice

def generate_number():
    random_number = random.randint(1, 9)
    return random_number