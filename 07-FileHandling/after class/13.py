# Write a program that computes the number of words in the following text. Use regular expressions.
# To be, or not to be, that is the question

import re

message = "To be, or not to be, that is the question"
letters = re.findall("\s{0}", message)

print(f"Text includes {len(letters) - 1} letters")