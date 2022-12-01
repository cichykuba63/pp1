arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

print("Numbers which don't repeat in second array: ", end = "")

for number in arr1:
    if arr2.count(number) == 0:
        print(number, end = " ")
    else:
        continue