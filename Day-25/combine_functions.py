from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Sum of squares of even numbers
result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

print(result)  # 56  (2² + 4² + 6²)
