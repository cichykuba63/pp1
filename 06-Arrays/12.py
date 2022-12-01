list = [[2, 5, 4], [9, 0, 3]]

for i in list[1]:
    print(i, end = " ")
    
for i in list:
    for n in i:
        print(n, end = " ")
    print()

for n in list:
    print(n[-1])