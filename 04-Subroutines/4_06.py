# Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. 
# Then call the function

def print_numbers():
    for i in range(1, 10):
        print(i, end = " ")

        if i == 3 or i == 6:
            print()

print_numbers()