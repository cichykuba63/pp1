# An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents of the array in reverse order. Use any loop statement. Sample result:
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15

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

    