zen_duplicated_file = open("texts/duplicated_chars.txt", "r")
a = zen_duplicated_file.readlines()
zen_duplicated_file.close()

for line in a:
    print(line[::2].rstrip())
