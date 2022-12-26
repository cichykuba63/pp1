# Write a program that calculates the number of lines for any text file. 
# The user enters the name of the file from the keyboard. 
# Display the result of the calculation (the file name and the number of lines). 
# Do not display the contents of the file. Sample result:
# File name: countries.txt
# Number of lines: 14

user_choice = input("Enter your file name with extension: ")
number_of_lines = 0

if user_choice.find(".") == -1:
    user_choice = user_choice + ".txt"

with open(user_choice.lower()) as file:
    for line in file:
        number_of_lines += 1

print(f"Your file: '{user_choice.lower()}' has {number_of_lines} lines.")