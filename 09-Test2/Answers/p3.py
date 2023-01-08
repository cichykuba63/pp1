def f(array2D):
    sum_arr = list()
    sum = 0

    for index in range(0, len(array2D[0])):
        for i in range(0, len(array2D)):
            sum += array2D[i][index]
        
        sum_arr.append(sum)
        sum = 0
    
    return sum_arr
