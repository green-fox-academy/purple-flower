from awesome.reverse import reverse_list
import os

print(reverse_list([3, 4, 5]))
print(os.getcwd())

alma_file = open("alma.txt")
print(alma_file.read())

alma_file = open("alma.txt", "w")
alma_file.write("Balozskam")
alma_file.close
