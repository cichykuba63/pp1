list = [1, 2, 3, 4, 5]

list[0] = list[0] - 1
print(list)

list[len(list) - 1] = list[len(list) - 1] + 4
print(list)

list[len(list) // 2] = list[len(list) // 2] * 2
print(list)

for element in range(len(list)):
    list[element] = list[element] + 3

print(list)
