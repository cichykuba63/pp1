# Write a program that calculates the number of vowels in the text:
# To be, or not to be, that is the question
# Use regular expressions and the findall() method.

import re

message = "To be, or not to be, that is the question"
vovels = re.findall("[aeiou]", message)

print(f"Number of vovels in the text is equal {len(vovels)}")