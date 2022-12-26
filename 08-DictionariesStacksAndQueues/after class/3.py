# Write the data to the students.json file. Then write a program that creates a limited.json file with the copy of the list of students, limited to data: first name, last name, student id.

import json

with open("students.json") as json_file:
    data = json.load(json_file)

limited_data = dict()

