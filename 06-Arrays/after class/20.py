# # Define a function that returns the elements of the array as a string, separated by commas. Using defined functions, display the contents of any array. Sample result:
# Array: [5,4,3,2,6,5]
# String: 5,4,3,2,6,5

def fun(array):
    str_arr = []
    
    for number in array:
        number = str(number)
        str_arr.append(number)
    
    print(f"Array: {array}")
    print(f"String: ", end = "")

    for i in str_arr:
        if str_arr[-1] == i:
            print(i, end = "")
            break
        print(i, end = ", ")
    print()

    return str_arr

print(fun([1, 2, 5, 10]))

