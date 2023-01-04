import re

statement = "To be, or not to be, that is the question"
sum = 0

words = re.findall("\w+", statement)

for element in words:
    sum += 1

print(f"Sum of words: {sum}")