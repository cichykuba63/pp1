arr = [15, 8, 31, 47, 2, 19]
x = -1
z = 0

for n in arr:
    if n == arr[0]:
        print("Array: ", end = "")
    print(n, end = " ")

while x != len(arr) - 1:
    x += 1
    z += arr[x]

z = z / len(arr)

print(f"\nArtithmetic mean: {round(z, 2)}")