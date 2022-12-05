# Write a program to find the second largest element in an array. Sample result:
# Array: [5,1,9,6,1]
# Result: 6

arr = [5, 1, 9, 6, 1, 20, 10, 5, 4, 2]
arr1 = []

print(f"Array: {arr}")

# Dodanie wartości niepowtarzających się z arr do arr1
for number in arr:
    if arr.count(number) == 1:
        arr1.append(number)
    else:
        if arr1.count(number) == 0:
            arr1.append(number)
        else:
            continue

arr1.sort()

print(f"Result: {arr1[-2]}")

