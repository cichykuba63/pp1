# The announcement regarding the temperature forecast in degrees Celsius for the next three days was published on the Internet:
# "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
# Create a program that calculates the average temperature. Use regular expressions to extract the values of temperatures from the message.

import re
import math

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}", message)
sum_of_temp = 0

for element in temperatures:
    sum_of_temp += int(element)

print(f"Average temperature is equal {math.floor(sum_of_temp / 3)}")
