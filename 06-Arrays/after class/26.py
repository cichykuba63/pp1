# A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. 
# Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. 
# Display the created array.

def create_2d_arr(x, y):
    arr = list()

    for _ in range(0, y):
        arr.append([])
    
    for a in range(0, y):
        for _ in range(0, x):
            arr[a].append("0")

    for e in arr:
        for i in e:
            print(i, end = " ")
        print()

create_2d_arr(3, 5)
        