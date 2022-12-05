# Create a program that displays all unique elements in an array. Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr = [1, 2, 1, 4, 2, 5, 7, 9]

print("Array: ", end = "")
for number in arr:              # Wypisanie wartości z array
    print(number, end = " ") 

print("\nUnique elements: ", end = "")
for n in arr:
    if arr.count(n) == 1:
        print(n, end = " ")     # Wypisanie elementów powtarzających się
    else:
        pass