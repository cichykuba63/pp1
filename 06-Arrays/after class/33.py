# Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that displays 1D array for the following 2D arrays.

def conversion(m):
    arr = []
    main_arr = m

    for element in main_arr:
        for argument in element:
            arr.append(argument)

    return arr

arr_one_dimension = conversion(([1, 2, 3], [4, 5, 6], [7, 8 , 9]))

for element in arr_one_dimension:
    print(element, end = " ")