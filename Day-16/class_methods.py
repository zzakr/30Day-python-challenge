class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

Employee.change_company("InnovateTech")
print(Employee.company)  # InnovateTech
