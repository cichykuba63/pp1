def minmax(array):
    arr = [min(array), max(array)]

    print("Array: ", end = "")
    for i in array:
        print(i, end = " ")

    print(f"\nResult: {arr}")

minmax([1, 2, 10, 5, 8])
        