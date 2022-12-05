# An array contains integer numbers: 12, 6, 4, 9, 10. Create a program that displays the array values graphically as below. Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.
# 12: ************
#  6: ******
#  4: ****
#  9: *********
# 10: **********

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

