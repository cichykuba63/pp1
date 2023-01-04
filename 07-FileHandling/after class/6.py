with open("text.txt") as file:
    with open("copylines.txt", "w") as file1:
        for line in file:
            file1.write(line)