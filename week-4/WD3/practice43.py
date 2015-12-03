filename = "alma.txt"
#write a function that reads a file and prints how many
#lines and characters in it


def lines_chars_counter(filename):
    input_file = open(filename)
    file_content = input_file.read()
    line_count = len(file_content.split("\n"))
    input_file.close()
    return[line_count, len(file_content)]

print(lines_chars_counter(filename))
