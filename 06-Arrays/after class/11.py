# Create a program that sorts elements of an array containing integer numbers. 
# Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and display any three arrays.

def bubblesort(array):
    
    for _ in range(0, len(array)):
        for number in range(0, len(array)):
            try:
                if array[number] < array[number + 1]:
                    pass
                else:
                    x = array[number + 1]
                    array[number + 1] = array[number]
                    array[number] = x
            except IndexError:
                pass
    return array

print(bubblesort([1, 2, 9, 4, 5, 2, 1, 2, 9, 1, 10, 2, 1, 20, 1, 2, 3, 1, 4]))