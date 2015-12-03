students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]
# create a function that counts the students that
# has more than 4 candies

"""def candy_calculator(list):
    output = []
    for student in list:
        if student["candies"] > 4:
            output.append(student)
    return output

print(len(candy_calculator(students)))"""


#2

def get_the_rich_mothers(list):
    rich_mothers = 0
    for kids in list:
        if kids["candies"] > 4:
            rich_mothers += 1
    return rich_mothers
print(get_the_rich_mothers(students))
