import re

statement = "To be, or not to be, that is the question"
sum = 0

vovels = re.findall("[aeiou]", statement)

for element in vovels:
    sum += 1

print(f"Sum of vovels: {sum}")
