# A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
# Write a program that finds N leading prime numbers. Read the value of N from the keyboard. 
# Using loop statements check that the number N is divisible only by 1 and by N

x = int(input("Enter your number: "))
y = int(x * 0.5 + 1)

for i in range(2, x+1):
    if i != 2 and i != 3 and i != 5 and i != 7 and i != 11:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
            print(i, end = " ")
    else:
        print(i, end = " ")

for n in range(2, y):
    if x % n == 0:
        x == False
        break
    else:
        x = True

if x == True:
    print("\nIt's a digit number.")
else:
    print("\nIt's not a digit number.")