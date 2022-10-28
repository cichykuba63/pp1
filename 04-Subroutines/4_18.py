# Define a function that calculates the sum of number digits. 
# Then use the function to calculate the sum of digits in the number 7182

def sum_of_digits():

    user_choice = str(input("Enter your number: "))
    suma = 0

    for letter in user_choice:    
        cyfra = int(letter)
        suma += cyfra

    print(suma)

sum_of_digits()