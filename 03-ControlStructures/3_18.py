# There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

user_choice = int(input("Enter your natural number: "))

division5 = user_choice // 5
division5_remainder = user_choice % 5

division2 = division5_remainder // 2
division2_remainder = division5_remainder % 2

division1 = division2_remainder // 1

print(f"""5 zł - {division5}
2 zł - {division2}
1 zł - {division1}""")