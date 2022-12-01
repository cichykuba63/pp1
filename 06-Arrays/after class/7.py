arr = [12, 6, 4, 9, 10]

for n in arr:
    for x in range(0, n, 1):
        if x == 0:
            print(f"{n}: ", end = "")
        print("*", end = "")
    print()

def star():
    z = str(sum(arr))
    return z

print(star())

