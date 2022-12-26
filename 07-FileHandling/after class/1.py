# The following program displays the contents of a file, line by line:
# f = open("filename.txt")
# for line in f:
#      print(line, end="")
# f.close()
# Rewrite the program using the "with ..." as construct. Then check that the program is working properly.

with open("filename.txt") as file:
    for line in file:
        print(line, end = "")