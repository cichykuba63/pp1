# Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate 
# line.

import random

with open("randomnumbers.txt", "w") as file:
    for _ in range(0, 50):
        file.write(str(random.randint(100, 999)) + "\n")
