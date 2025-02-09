from functools import reduce

numbers = [1, 2, 3, 4]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)

print(total)  # 10
