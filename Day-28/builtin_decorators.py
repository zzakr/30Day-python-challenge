class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def description(cls):
        return f"{cls.__name__} performs basic math operations"

print(MathOperations.add(5, 3))        # 8
print(MathOperations.description())   # MathOperations performs basic math operations
