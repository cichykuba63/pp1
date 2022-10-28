# Create a program that calculates how many times the given letter appears in any text. 
# Then create a program and check how many times the letter e’ appears in the text below. 
# Define a function for making calculations

def letter():
    user_choice = str(input("Enter a letter: "))
    x = 0
    text = "You never get a second chance to make a first impression"

    for i in text:
        if user_choice == i:
            x += 1
    
    print(f"Letter '{user_choice}' was used {x} times")

letter()