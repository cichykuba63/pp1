list = [-15, 8, -31, 47, -2, 19]
min = list[0]
max = list[0]

for number in list:
    if number > max:
        max = number
    if number < min:
        min = number

print(f"Min value: {min}")
print(f"Max value: {max}")
