with open("power.txt", "w") as file:
    for number in range(1, 11):
        for power in range(1, 4):
            file.write(f"{number ** power}, ")
        file.write("\n")