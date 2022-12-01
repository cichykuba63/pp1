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

