# Display both arrays and the result of comparison. Sample result:
# Array1: water book sky
# Array2: water book sky
# Comparison: arrays are the same

def compare(array1, array2):
    comparison = None

    print("Array1: ", end = "")
    for n in array1:    
        print(n, end = " ")

    print()

    print("Array2: ", end = "")
    for n in array2:
        print(n, end = " ")

    print()

    if len(array1) == len(array2):
        pass
    else:
        comparison = False
    
    for x in range(0, len(array1)):
        if array1[x] == array2[x]:
            continue
        else:
            comparison = False
            
    if comparison == True:
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")



compare([True,False], [True,False,True])

    
    