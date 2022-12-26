# Create a program that writes to a text file integer numbers in the range of <1,50>, every number in a 
# separate line.

with open("integers.txt", "w") as file:
    for number in range(1, 51):
        number = str(number)
        file.write(number + "\n")