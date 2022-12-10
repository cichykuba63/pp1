file = open("shopping.txt", "a", encoding = "utf-8")

while True:
    user_choice = input("\nEnter the name of product: ")

    if user_choice == "":
        break

    file.write(user_choice + "\n")

file.close()