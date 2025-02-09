zipped_data = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

names, scores = zip(*zipped_data)

print(names)  # ('Alice', 'Bob', 'Charlie')
print(scores)  # (85, 90, 78)

