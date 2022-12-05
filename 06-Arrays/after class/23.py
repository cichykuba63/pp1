# Define a function rand_elem(array) that returns a randomly selected array element. 
# Using the function, display a few randomly selected array elements

import random

def rand_elem(array):
    return random.choice(array)

print(rand_elem([5, 4, 2, 1]))
