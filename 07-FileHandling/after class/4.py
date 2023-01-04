count = 0

with open("numbers1.txt", "w") as file:
    for i in range(1, 101):
        file.write(f"{i}\n")

with open("numbers1.txt") as file:
    for line in file:
        if count != 0 and count % 5 == 0:
            input("Enter any key to proceed.")
        count += 1
        print(line.strip())