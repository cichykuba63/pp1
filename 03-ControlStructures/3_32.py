# Write a program that displays a lottery coupon (numbers from 1 to 49) in the format as below.

for n in range(0, 7):
    print()
    for i in range(1, 50, 7):
        if n >= 1:
            print(i + n, end = " ")
        else:
            print(i, end = " ")

print("\n")

