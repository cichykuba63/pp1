# Write a program that, for the given array of real numbers, 
# displays the number of elements that are greater than the given value entered from the keyboard

arr = [1, 6, 8.2, 9.5, 10, 12.3, 20]
user_choice = float(input("Enter your real number: "))

print(f"Array: {arr}")
print("Your number is greater than: ", end = "")
for number in arr:
    if user_choice > number:
        print(number, end= " ")
