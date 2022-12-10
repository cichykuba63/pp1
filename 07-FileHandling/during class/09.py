file = open("numbers.txt", "rt")
sum_of_integers = 0

for line in file:
    sum_of_integers += int(line)

print(f"Sum = {sum_of_integers}")

file.close()
