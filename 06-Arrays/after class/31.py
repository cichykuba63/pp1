# Create a function identity_matrix(n) that returns an identity matrix of size n 
# Then create a function that displays a 2D array in rows and columns.
# Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8.

def identity_matrix(n):
    arr = []
    x = -1

    if n == 1:
        arr.append(1)
    else:
        for _ in range(0, n):
            arr.append([])
        for argument in arr:
            x += 1
            for _ in range(0, n):
                argument.append(0)
            argument.insert(x, 1)
            argument.pop(x + 1)
    
    return arr

def arr_display(arr):
    for element in arr:
        for argument in element:
            print(argument, end = " ")
        print()


first_matrix = identity_matrix(4)






