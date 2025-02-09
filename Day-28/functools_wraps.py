from functools import wraps

def decorator_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorator_function
def example():
    """This is the example function"""
    print("Executing example function")

print(example.__name__)  # example
print(example.__doc__)   # This is the example function
