# Find any text file on the Internet and download it to your computer. Then write a program that copies the 
# contents of this file to the copylines.txt file. Copy the contents of the file line by line. Finally, open 
# both files in any text editor and check that their contents are the same.

with open("file.txt") as file:
    with open("copylines.txt", "w") as file1:
        for line in file:
            line_content = file.readline()
            file1.write(line_content)