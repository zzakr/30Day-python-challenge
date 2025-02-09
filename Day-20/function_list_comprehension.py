def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared = [square(num) for num in numbers]

print(squared)  # [1, 4, 9, 16]
