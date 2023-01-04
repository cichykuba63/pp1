import json

count = 0
dic = dict()

with open("students.json") as file:
    content = json.load(file)


with open("limited.json", "w") as file1:
    for row in content:
        for k, v in row.items():
            count += 1

            if count == 1 or count == 2 or count == 3:
                dic[k] = v
            
        count = 0    
        json.dump(dic, file1, indent = 4)
            
            