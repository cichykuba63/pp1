# The array contains integer numbers from 1 to 999. 
# Write a program that displays elements of the array formatted as below.

arr = [1, 5, 20, 100, 500, 620, 920, 999]

print()
print("-" * 41)

for number in arr:
    if number == arr[len(arr) - 1]:
        print(f"| {number}|", end = "")
        break
    if number < 10:
        print(f"|   {number}", end = "")
    elif number < 100 and number >= 10:
        print(f"|  {number}", end = "")
    else:
        print(f"| {number}", end = "")

print() 
print("-" * 41)
print()
