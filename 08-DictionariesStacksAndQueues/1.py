import json

with open("data.json") as file:
    content = json.load(file)

for data in content:
    for k, v in data.items():
        print(f"{k}: {v}")