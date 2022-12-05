# Write a program to separate even and odd numbers of a given array of integers. 
# Put all even numbers first, and then odd numbers.

arr = [1, 2, 4, 5, 7, 8, 9, 10, 11]
arr_ordered = []

# Dodanie wartości parzystych
for number in arr:
    if number % 2 == 0:
        arr_ordered.append(number)
        
# Dodanie wartości nieparzystych
for number in arr:
    if number % 2 != 0:
        arr_ordered.append(number)

print(f"Wartości: {arr_ordered}")