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
    

