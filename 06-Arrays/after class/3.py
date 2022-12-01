arr = [8, 2, 5, 1, 9]

for n in arr:
    if n == arr[0]:
        print("Array: ", end = "")
    print(n, end = " ")

for n in arr:
    if n == arr[0]:
        print("\n2nd power: ", end = "")
    n = pow(n, 2)
    print(n, end = " ")