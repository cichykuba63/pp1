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