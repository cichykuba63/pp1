# Create a program that saves to a text file, numbers in the range of <1,10> with their second and third power.

with open("powerintegers.txt", "w") as file:
    for number in range(1, 11):
        for power in range(1, 4):
            powered_number = number
            powered_number **= power
            file.write(str(powered_number) + ", ")
        
        file.write("\n")
