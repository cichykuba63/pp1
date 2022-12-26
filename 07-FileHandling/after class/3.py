# Find any text file on the Internet that contains at least 30 lines of text and download that file 
# to your computer. Then write a program that displays the first five lines from the file and then 
# waits for the Enter key to be pressed. Then repeat displaying the next five lines from the file, 
# waiting for the Enter key to be pressed each time.

file = open("file.txt", encoding = "utf-8")
x = 0

for line in file:
    x += 1
    if x % 5 == 0:
        stop = input("\nPress enter to continue ")
    print("\n" + line.strip())
    
file.close()