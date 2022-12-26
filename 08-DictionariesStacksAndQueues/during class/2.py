mobile_phone = {
    "price": 2000,
    "colour": "black",
    "size": 9.5,
    "working": True,
    "number": "572810284",
    "parameters": {"processor": "good", "graphic": "2gb"}
}

count = 0
x = 0

for key, value in mobile_phone.items():
    print(key + ":", value)
