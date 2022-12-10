file = open("countries.txt", "rt")

for line in file:
    print(line, end = "")

file.close()
