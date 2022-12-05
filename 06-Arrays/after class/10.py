# Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
# Create a program that displays the numbers from the first array that do not appear in the second array.

arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

print("Numbers which don't repeat in second array: ", end = "")

for number in arr1:
    if arr2.count(number) == 0:
        print(number, end = " ")
    else:
        continue