class A:
    def method_A(self):
        return "A method"

class B:
    def method_B(self):
        return "B method"

class C(A, B):
    pass

obj = C()
print(obj.method_A())  # A method
print(obj.method_B())  # B method
