# Create a dictionary where you put all the letters and the corresponding words. Then try to spell your name and three other words.  

letters = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform"
}

user_text = input("Enter your text: ").upper()
translated_text = ""

for letter in user_text:
    translated_text += letters[letter]
    if letter.index == len(user_text) - 1: #przy ostatnim nie dodajemy spacji
        break
    translated_text += " "

print(f"Translated text: {translated_text}")



