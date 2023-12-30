class Employee : 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Alternative constructor 
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e = Employee("Mizan", 12000)
print(e.name, e.salary)

f = Employee.fromStr("Johurul-1200") # new instance with different format with class method
print(f.name, f.salary)