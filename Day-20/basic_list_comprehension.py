# Traditional way using a for loop
numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num ** 2)

print(squared)  # [1, 4, 9, 16, 25]

# Using list comprehension
squared = [num ** 2 for num in numbers]
print(squared)  # [1, 4, 9, 16, 25]
