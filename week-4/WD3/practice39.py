names = ["Zakarias", "Hans", "Otto", "Ole"]
# create a function that returns the shortest string from a list

def shortest_string(list):
    output = list[0]
    for str in list:
        if len(output) > len(str):
            output = str

    return output
print(shortest_string(names))
