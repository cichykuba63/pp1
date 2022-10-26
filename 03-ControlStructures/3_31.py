# Write a program that displays 20 integer random numbers in the range of 5 to 10

import random

for i in range(1, 21, 1):
    print(random.randint(5, 10), end = " ")
