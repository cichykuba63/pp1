sum = 0

with open("numbers.txt") as file:
    for line in file:
        sum += 1

print(f"Sum of lines: {sum}")