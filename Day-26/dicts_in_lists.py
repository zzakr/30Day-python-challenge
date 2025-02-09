students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"}
]

# Accessing elements
print(students[1]["name"])  # Bob

# Iterating through the list of dictionaries
for student in students:
    print(f"{student['name']} is {student['age']} years old and got grade {student['grade']}.")
