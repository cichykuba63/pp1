person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123523214", "mobile": "604525128"}
}

for x, y in person.items():
    print(x + ": ", y)

print()

print(person["name"])

print()

for value in person["hobby"]:
    print(value)

print()

person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobby"] += ["bicycle"]
person["phone"]["work phone"] = "472910482"

print(person)