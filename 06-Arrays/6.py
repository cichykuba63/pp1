list = [2, 3, 7, 5, 4]
print(f"list elements:{list}")
print(f"Number of elements: {len(list)}")
print(f"First value: {list[0]}")
print(f"Second value: {list[1]}")
print(f"Last value: {list[-1]}")
print(f"Last but one value: {list[-2]}")
print(f"Sum of the first and last value: {list[0] + list[-1]}")
print(f"Middle value: {list[len(list) // 2]}")

for element in list:
    print(element, end = " ")
print()
for element in range(len(list) // 2 + 1):
    print(list[element], end = " ")


