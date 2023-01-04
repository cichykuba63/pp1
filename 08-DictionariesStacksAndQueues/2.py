import json

dic = {
    "color": "black",
    "price": 50,
    "is_available": True,
    "readed": False,
    "pages": 200
}

with open("favourite.json", "w") as file:
    json.dump(dic, file, indent=4)