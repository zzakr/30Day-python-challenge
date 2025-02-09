def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Access granted.")

check_age(16)  # This will raise an error
