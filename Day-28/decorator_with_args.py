def repeat_decorator(times):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            for _ in range(times):
                original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
