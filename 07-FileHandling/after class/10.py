import csv

file = open("students.txt")

content = csv.reader(file, delimiter=",")
count = 1

for line in content:
    if count == 1:
        count += 1
        continue

    if int(line[2]) < 30:
        print(f"{line[0]}\t{line[1]}\t{line[4]}")


file.close()