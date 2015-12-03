zen_reversed_file = open("texts/reversed_zen_order.txt", "r")
a = zen_reversed_file.read()
zen_reversed_file.close()

lines = a.split("\n")

reversed_lines = lines[::-1]

result = "\n".join(reversed_lines)

print(result)
