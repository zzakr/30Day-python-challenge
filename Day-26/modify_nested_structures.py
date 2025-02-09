students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"}
]

# Updating values
students[0]["grade"] = "A+"
print(students[0]["grade"])  # A+

# Adding new entries
company = {"departments": {"IT": {"employees": 10, "budget": 50000}}}
company["departments"]["Finance"] = {"employees": 8, "budget": 40000}
print(company["departments"])
