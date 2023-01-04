with open("text.txt") as file:
    content = file.read()

with open("copylines.txt", "w") as file1:
    file1.write(content)