ag = "kuty"

"""write a function that gets a string as an input and appends an 'a' character to its end"""

def new_text(string):
    return string + "a"

ag = new_text(ag)
print(ag)


ag2 = ["rep", "macsk", "cic", "alm", "Ann", "kacs" ]

for i in range(len(ag2)):
    ag2[i] = new_text(ag2[i])
    
print(ag2)
