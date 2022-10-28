# Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year.
# Define a function month(n) that returns a month name based on the month number (values from 1 to 12). 
# Then create a program and display the name of the month 7.

def month(n):
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3:
        print("March")
    elif n == 4:
        print("April")
    elif n == 5:
        print("May")
    elif n == 6:
        print("June")
    elif n == 7:
        print("July")
    elif n == 8:
        print("August")
    elif n == 9:
        print("September")
    elif n == 10:
        print("October")
    elif n == 11:
        print("November")
    elif n == 12:
        print("December")

month(7)