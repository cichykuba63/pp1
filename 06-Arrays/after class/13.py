
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
