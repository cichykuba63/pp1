import random

with open("integers.txt", "w") as file:
    for _ in range(50):
        file.write(f"{random.randint(100, 999)}\n")