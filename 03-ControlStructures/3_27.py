# A computer numeric keyboard has the arrangement of the keys as below. 
# The included program code displays the computer keyboard. 
# Analyse the program in terms of the displayed results. 
# Do you understand each program statement? Then make a change in your program code. Replace the ‘for’ with a ‘while’ statement

# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f' {i+j}',end='')
#     print()

y = 0

while y != 9:

    for i in range(7, 10):
        print(i, end = " ")
        y += 1
    print()
    for j in range(4, 7):
        print(j, end = " ")
        y += 1
    print()
    for n in range(1, 4):
        print(n, end = " ")
        y += 1
    
