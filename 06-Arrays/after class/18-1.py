# Create a function minmax(array) that, for the given array of integers, 
# returns a two-element array containing the smallest and largest values in the given array. Sample result:
# Array:  [4,2,8,4,7,9,5]
# Result: [2,9]

def minmax(array):
    arr = [min(array), max(array)]

    print("Array: ", end = "")
    for i in array:
        print(i, end = " ")

    print(f"\nResult: {arr}")

minmax([1, 2, 10, 5, 8])
        