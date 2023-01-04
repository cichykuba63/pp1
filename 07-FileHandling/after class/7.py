with open("MeatAndFish.txt") as file:
    content1 = file.read()

with open("GrainsAndBread.txt") as file1:
    content2 = file1.read()

with open("shoppinglist.txt", "w") as file2:
    file2.write(content1)
    file2.write(content2)