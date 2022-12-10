person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#a
for keys, values in person.items():
    print(f"{keys}: {values}")

#b
print(person["name"])

#c
for element in person["hobby"]:
    print(element, end = " ")

#d
person["surname"] = "Nowak"

#e
person["married"] = False

#f
person["gender"] = "male"

#g
person["hobby"] += ["bicycle"]

#h
person["phone"]["work"] = "313131444"
print(person)