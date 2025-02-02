def show_details(*args, **kwargs):
    for arg in args:
        print("Positional argument:", arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(1, 2, 3, name="Alice", age=25)
