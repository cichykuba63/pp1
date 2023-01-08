import json

with open("..\data.json") as file:
    content = json.load(file)


def f(age, course, average):
    sum_of_grades = 0; students = 0

    for student in content:
        if student["age"] >= age:
            for index in range(0, len(student["studies"]["courses"])):
                if student["studies"]["courses"][index]["name"] == course:
                    for data in student["studies"]["courses"]:
                        if data["name"] == course:
                            sum_of_grades = 0
                            for grade in data["grades"]:
                                sum_of_grades += grade

                            if round(sum_of_grades / len(data["grades"]), 2) >= average:
                                students += 1
                            else:
                                break
            else:
                continue

    return students
    