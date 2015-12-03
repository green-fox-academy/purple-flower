output_file = open("write.txt", "w")
zen_encoded_file = open("texts/encoded_zen_lines.txt", "r")
a = zen_encoded_file.readlines()


original_text = ""
for line in a:
    splitted_lines = line.split(" ")
    original_line = ""
    for word in splitted_lines:
        original_word = ""
        for char in word:
            original_word += chr(ord(char)-1)
        original_line += original_word + " "
    original_text += original_line + "\n"

output_file.write(original_text)

zen_encoded_file.close()
output_file.close()
