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