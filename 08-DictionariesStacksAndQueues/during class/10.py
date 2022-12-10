countries = [
    {"country":"France", "population":67500000},
    {"country":"Portugal", "population":10300000},
    {"country":"Poland", "population":37780000},
    {"country":"Russia", "population":143400000},
    {"country":"China", "population":1412000000},
]

for element in countries:
    for c, v in element.items():
        print(f"{c}: {v}")
    print()

