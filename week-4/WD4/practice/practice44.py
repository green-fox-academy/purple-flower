filename = "alma.txt"


#2
def print_file_lines_with_a2(name):
    file_to_print = open(name)
    lines = file_to_print.readlines()
    file_to_print.close()

    output = ''
    for line in lines:
        print("a" + line.rstrip())

print_file_lines_with_a2(filename)
