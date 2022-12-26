# Create a function transpose_matrix(m) that returns transposed matrix m. 
# Then create a program that displays transposed matrices, in rows and columns, for the following matrices.

def transpose_matrix(m):
    main_arr = m
    arr = []

    try:
        for _ in main_arr[0]:
            arr.append([])
        for i in range(0, len(main_arr[0])):
            for element in main_arr:
                arr[i].append(element[i])
    except TypeError:
        for _ in m:
            arr.append([])
        for i in range(0, len(m)): 
            arr[i].append(m[i])

    return arr

function_value = transpose_matrix([1, 2, 3])

for element in function_value:
    for argument in element:
        print(argument, end = " ")
    print()
        