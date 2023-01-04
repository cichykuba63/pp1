import stack
import string

operators = list(string.punctuation)

while True:
    user_choice = input("Enter number or sign(+ - * / =): ")

    try:
        number = int(user_choice)
        stack.push(number)

    except ValueError:
        if user_choice == operators[18]:
            break

        first_value = stack.pop()
        second_value = stack.pop()

        if user_choice == operators[9]:
            stack.push(first_value * second_value)
        elif user_choice == operators[10]:
            stack.push(first_value + second_value)
        elif user_choice == operators[12]:
            stack.push(first_value - second_value)
        elif user_choice == operators[14]:
            stack.push(first_value / second_value)

print("\nResult: ", end = "")
stack.display()
