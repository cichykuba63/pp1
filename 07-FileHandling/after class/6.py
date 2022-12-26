# Using any text editor, create the following two text files:

# MeatAndFish.txt
# GrainsAndBread.txt

# Then write a program that creates a shoppinglist.txt file, in which save the contents of the MeatAndFish.txt 
# and the GrainsAndBread.txt files.

main_file = open("shoppinglist.txt", "a")
file1 = open("Meatandfish.txt")
file2 = open("GrainsAndBread.txt")

file1_content = file1.read()
file2_content = file2.read()

main_file.write(file1_content + "\n")
main_file.write(file2_content)

file2.close()
file1.close()
main_file.close()