import stack

user_choice = int(input("Natural number: "))

integer_part = user_choice
number = -1

while number != 0:
    number = integer_part
    if number != 1:
        integer_part = number // 2
        remainder = number % 2
        stack.push(remainder)
    else:
        stack.push(1)
        break

print("Binary number: ", end = "")
for _ in range(len(stack.stack)):
    print(stack.pop(), end = "")
    
    