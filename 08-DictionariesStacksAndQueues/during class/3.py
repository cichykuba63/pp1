import json

with open("plik.json") as file:
    data = json.load(file)

for key, value in data.items():
    print(key, ":", value)