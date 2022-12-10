arr = ["SWAT", "Cry of Fear", "Forest Gump", "Avatar", "Foreigners"]

file = open("filmtitles.txt", "w", encoding = "utf-8")

for element in arr:
    file.write(element + "\n")

file.close()

