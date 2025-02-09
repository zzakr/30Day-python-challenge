matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][1])  # 2 (row 0, column 1)

# Iterating through nested lists
for row in matrix:
    for value in row:
        print(value, end=" ")  # 1 2 3 4 5 6 7 8 9
