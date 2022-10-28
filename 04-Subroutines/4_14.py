# Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg and height in cm. 
# Then calculate BMI for Peter (81kg, 182cm).

bmi = lambda x, y: round(x * (y * 0.01) ** 2, 2)

print(bmi(81, 182))