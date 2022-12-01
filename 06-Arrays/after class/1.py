arr = [15, 8, 31, 47, 2, 19]

for n in arr:
    if n == arr[0]:
        print("Existed array: ", end = "")
    print(n, end = " ")

a = arr.reverse()

for n in arr:
    if n == arr[0]:
        print("\nReverse array: ", end = "")
    print(n, end = " ")

    