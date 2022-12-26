# Find any text file on the Internet and download it to your computer. Then write a program that displays all words with at least six letters from the file. Display each word on a separate line. Use regular expressions.

import re

with open("file.txt", encoding = "utf-8") as file:
    file_content = file.read()

all_words = re.findall("\S+", file_content) #looking all words
words = [] #for adding 5-letter-long words

for element in all_words:
    if len(element) >= 5:
        words.append(element)

#deleting . , : -
for element in words:
    word_index = words.index(element)
    if element.find(",") != -1:
        index = element.index(",")
        if index == 0:
            element = element[1:]
            words.insert(word_index, element)
            words.pop(word_index + 1)
        else:
            element = element[0:index]
            words.insert(word_index, element)
            words.pop(word_index + 1)

    elif element.find(".") != -1:
        index = element.index(".")
        if index == 0:
            element = element[1:]
            words.insert(word_index, element)
            words.pop(word_index + 1)
        else:
            element = element[0:index]
            words.insert(word_index, element)
            words.pop(word_index + 1)

    elif element.find(":") != -1:
        index = element.index(":")
        if index == 0:
            element = element[1:]
            words.insert(word_index, element)
            words.pop(word_index + 1)
        else:
            element = element[0:index]
            words.insert(word_index, element)
            words.pop(word_index + 1)

    elif element.find("-") != -1:
        index = element.index("-")
        if index == 0:
            element = element[1:]
            words.insert(word_index, element)
            words.pop(word_index + 1)
        else:
            element = element[0:index]
            words.insert(word_index, element)
            words.pop(word_index + 1)

for element in words:
    print(element)