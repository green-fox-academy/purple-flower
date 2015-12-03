zen_reversed_file = open("texts/reversed_zen_lines.txt", "r")
a = zen_reversed_file.readlines()
zen_reversed_file.close()


for line in a:
    print(line[::-1], end = "")
