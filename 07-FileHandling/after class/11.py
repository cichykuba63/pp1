import re

statement = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperature = re.findall("\d{2}", statement)

print(f"Sum of temperatures: {int(temperature[0]) + int(temperature[1]) + int(temperature[2])}")