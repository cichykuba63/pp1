# Write a program that displays the difference between the largest and smallest values in an array of integers.
# Sample result:
# Array: [5,1,9,6,1]
# Result: 8

arr = [5, 1, 9, 6, 1]
max_value = max(arr)
min_value = min(arr)

print(f"Array: {arr}")
print(f"Result: {max_value - min_value}")

