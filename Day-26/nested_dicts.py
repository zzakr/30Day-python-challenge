company = {
    "departments": {
        "IT": {"employees": 10, "budget": 50000},
        "HR": {"employees": 5, "budget": 20000}
    }
}

# Accessing elements
print(company["departments"]["IT"]["employees"])  # 10

# Iterating through nested dictionaries
for dept, details in company["departments"].items():
    print(f"{dept} has {details['employees']} employees and a budget of {details['budget']}.")
