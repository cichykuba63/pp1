# Then create a program that reads data from the CSV file and displays the first name, last name and email address of students under 30. Format the data as below. 

import csv

with open("students.txt") as file:
    file = csv.reader(file, delimiter = ",")
    line_count = 0
    print()
    for line in file:
        if line_count == 0:
            line_count += 1
            continue
        else:
            if int(line[2]) >= 30:
                continue
            else:
                print(f"{line[0]}\t{line[1]}\t{line[4]}")
    print()
