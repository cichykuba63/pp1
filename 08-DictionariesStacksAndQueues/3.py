import json

dic = {
    "student1": {
        "firstname": "Andrzej",
        "surname": "Duda",
        "age": 26,
        "married": False,
        "phone": {
            "workphone": "604259201",
            "homephone": "602010241"
        }
    },
    "student2": {
        "firstname": "Marian",
        "surname": "Paździoch",
        "age": 30,
        "married": True,
        "phone": {
            "workphone": "432819203",
            "homephone": "128219321"
        }
    }
}

with open("student.json", "w", encoding = "utf-8") as file:
    json.dump([dic], file, indent=4, ensure_ascii=False)