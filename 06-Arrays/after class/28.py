# An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. 
# Create a program that finds the smallest and largest values in the array 
# and in which row and column they are located.

arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
min_value = None
max_value = None

for a in arr:
    for number in a:
        if max_value == None or number > max_value:
            max_value = number
        if min_value == None or number < min_value:
            min_value = number

for a in arr:
    for number in a:
        if number == max_value:
            print(f"Max value {min_value} is located in {arr.index(a) + 1} row and {a.index(number) + 1} column")
        if number == min_value:
            print(f"Min value {max_value} is located in {arr.index(a) + 1} row and {a.index(number) + 1} column")