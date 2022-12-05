# Define a median(array) function that returns the median of the given array of numbers. 
# Do not use built-in functions. The median is the middle value in the ordered sequence of numbers 
# Then, using the defined function, calculate and display the median for the following values:
# a.	[1,0,9,4,6]
# b.	[6,8,3,1,0,5,7]

from math import *

def median(array):
    print(f"Array: {array}")
    array.sort()
    print(f"Sorted array: {array}") # Posortowana array

    if len(array) % 2 != 0:
        print(f"Median value: {array[floor(len(array) / 2)]}")
    else:
        print(f"Median value: {(array[len(array) / 2 - 1] + array[len(array / 2)]) / 2}")

median([1, 0, 9, 4, 6])
print()
median([6, 8, 3, 1, 0, 5, 7])