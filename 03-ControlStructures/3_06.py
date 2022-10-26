# The speed limit on the motorway is 130 km / h. Write a program that checks whether a car exceeded the speed limit.

user_speed = int(input("Insert your speed in km/h: "))
speed_limit = 130

if user_speed > speed_limit:
    print("Your speed is too high!")
elif user_speed == speed_limit:
    print("Your speed is equal to speed limit")
else:
    print("Your speed is good.")
