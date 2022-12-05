# Write a program that checks whether the first array is a subset of the second one 
# (whether all elements of the first array appear in the second array).

def checking(arr, arr1):
    
    for number in arr1:
        if arr.count(number) != 0:
            pass
        else:
            return False
        
    return True

print(checking([1, 2, 5, 9, 10, 11, 12], [1, 2, 5, 9, 10, 11]))
