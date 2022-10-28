# Define a function sum(N) that for the given natural number N calculates the sum of all natural numbers between 1 and N. 
# Apply recursion. Then create a program that calculates the sum of natural numbers in the range <1,10>.

def sum(n):
    x = 0
    for i in range(1, n):
        x += i
    return x

y = 20
print(f"\nSum of numbers between 1 and {y}: {sum(y)}\n")
