# Define a function occurs(number, array) that returns True if a given number is present in an array. 
# Then create a program that checks whether the number entered from the keyboard is present 
# in the array [15, 38, 7, 23, 14]. Sample result:
# Number: 23
# Array: 15 38 7 23 14
# Result: number 23 appears in the array

user_choice = int(input("Enter your number: "))
arr = [1, 2, 6, 9, 10]

def occurs(number, array):
    if not array.count(number) >= 1:
        return False
    else:
        return True

# Wypisanie wybranego numeru
print(f"\nNumber: {user_choice}")

# Wypisanie elementów listy
print("Array: ", end = "")
for number in arr:
    print(number, end = " ")

# Wypisanie rezultatu
print("\nResult: ", end = "")
if occurs(user_choice, arr) == True:
    print(f"Number {user_choice} appears in array")
else:
    print(f"Number {user_choice} doesn't appear in array")
