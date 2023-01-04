file = open("shopping.txt", "a", encoding = "utf-8")

user_choice = input("Add product: ")
file.write(user_choice + '\n')

file.close()