# Let x and y denote the coordinates of a point on the plane. 
# Write a program that determines in which quadrant of the coordinate system the point P (x, y) is located
# or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

while True:
    try:
        print()

        x = int(input("Enter the x number: "))
        y = int(input("Enter the y number: "))

        print()
        print(f"Selected x: {x}\nSelected y: {y}")
        print()

        if x > 0 and y > 0:
            print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
        elif x < 0 and y > 0:
            print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
        elif x < 0 and y < 0:
            print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
        elif x > 0 and y < 0:
            print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
        elif x == 0 and y != 0:
            print(f"Point P({x},{y}) is located in the axis Y")
        elif y == 0 and x != 0:
            print(f"Point P({x},{y}) is located in the axis X")
        elif x == 0 and y == 0:
            print(f"Point P({x},{y}) is located in point (0,0)")
        
    except:
        print("Something went wrong. Try again")