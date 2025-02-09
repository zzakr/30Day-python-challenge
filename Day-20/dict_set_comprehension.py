# Dictionary comprehension
numbers = [1, 2, 3]
squared_dict = {num: num ** 2 for num in numbers}

print(squared_dict)  # {1: 1, 2: 4, 3: 9}

# Set comprehension
unique_numbers = {num for num in [1, 2, 2, 3, 3, 3]}
print(unique_numbers)  # {1, 2, 3}
