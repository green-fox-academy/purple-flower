students = [
    {"name": "Tibi", "age": 8},
    {"name": "Adorjan", "age": 9},
    {"name": "Agoston", "age": 6},
    {"name": "Aurel", "age": 7},
    {"name": "Dezso", "age": 12},
]

students_at_least_8 = []

for item in students:
    if item["age"] >= 8:
        students_at_least_8.append(item["name"])

print(students_at_least_8)



students_names_starting_with_A = []

for item in students:
    if item["name"][0] == "A":
        students_names_starting_with_A.append(item["name"])

print(students_names_starting_with_A)
