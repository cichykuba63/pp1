arr = [5, 1, 9, 6, 1]
max_value = None
min_value = None

for number in arr:
    if max_value == None or number > max_value:
        max_value = number
    if min_value == None or number < min_value:
        min_value = number

print(f"Array: {arr}")
print(f"Result: {max_value - min_value}")