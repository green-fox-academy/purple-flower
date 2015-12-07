import re

def filereader():
    with open("regex.txt", "r") as inp:
        text = inp.read()
        v = re.sub(r'mit', 'mire', text)
        print(v)

filereader()
