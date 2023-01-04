import re

count = 0
sum = 0

with open("grades.txt") as file:
    for line in file:
        line = line.strip()
        count += 1
        if count == 2:
            peter_grades = re.findall("\d.\d", line)
        elif count == 5:
            anna_grades = re.findall("\d.\d", line)

for element in peter_grades:
    sum += float(element)

peter_average = sum / len(peter_grades)
sum = 0

for element in anna_grades:
    sum += float(element)

anna_average = sum / len(anna_grades)

print(f"Arithmetic mean of Anna's grades: {round(anna_average, 2)}")
