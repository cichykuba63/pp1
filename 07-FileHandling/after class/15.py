# Then create a program that calculates the arithmetic mean of student’s grades.

import re

file = open("grades.txt")

sum_of_grades1 = 0
sum_of_grades2 = 0
line_count = 1

for line in file:
    if line_count != 2 and line_count != 5:
        line_count += 1
        continue
    if line_count == 2:
        peter_grades = re.findall("\d.\d", line)
        line_count += 1
    if line_count == 5:
        anna_grades = re.findall("\d.\d", line)

file.close()

for element in peter_grades:
    sum_of_grades1 += float(element)

for element in anna_grades:
    sum_of_grades2 += float(element)

print(f"Arithmetic mean of peter grades is equal {round(sum_of_grades1 / len(peter_grades), 2)}")
print(f"Arithmetic mean of anna's grades is equal {round(sum_of_grades2 / len(anna_grades), 2)}")