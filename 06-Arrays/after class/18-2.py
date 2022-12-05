# Create a function minmax(array) that, for the given array of integers, 
# returns a two-element array containing the smallest and largest values in the given array. Sample result:
# Array:  [4,2,8,4,7,9,5]
# Result: [2,9]



def minmax(array):
    min_value = None
    max_value = None
    arr = []

    print(f"Array: {array}")

    for number in array:
        if min_value == None or number < min_value:
            min_value = number
        if max_value == None or number > max_value:
            max_value = number

    arr.append(min_value)
    arr.append(max_value)

    print(f"Result: {arr}")

minmax([1, 5, 9, 10, 11])
    

