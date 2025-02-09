lines = ["Python is fun\n", "File handling is easy\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)
