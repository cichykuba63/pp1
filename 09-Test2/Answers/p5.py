def f(first_letter, last_letter):

    words_first_letter = 0; words_last_letter = 0

    with open("..\data.txt", encoding = "utf-8") as file:
        for line in file:
            line = line.split()
            for word in line:
                if word.startswith(first_letter):
                    words_first_letter += 1
                if word.endswith(last_letter):
                    words_last_letter += 1

    return words_first_letter, words_last_letter
print(f('w','d'))