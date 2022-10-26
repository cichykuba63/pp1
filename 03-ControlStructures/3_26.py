# The payment card is secured with a four-digit PIN code (0805). 
# Write a program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked.

no_of_tries = 3

while no_of_tries != 0:
    pin_code = "0805"
    print()
    user_pin = str(input(f"Enter your PIN number ({no_of_tries} tries): "))

    if user_pin == pin_code:
        print("Password is correct. Access granted.")
        break
    else:
        no_of_tries -= 1
        print(f"Password is incorrect.")
        
        if no_of_tries != 0:
            print(f"Remaining tries: {no_of_tries}")

if no_of_tries == 0:
    print("Your card has been blocked.")
    print()


