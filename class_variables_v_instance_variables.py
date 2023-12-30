
class Employee:
    company_name = "Apple" # class variable, not instance variable
    numberOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.numberOfEmployees += 1

    def showDetals(self):
        print(f"The name of the employee is {self.name} and raise amount in {self.company_name} sized {self.numberOfEmployees} is {self.raise_amount}")


m = Employee("Mizan")
m.raise_amount = 0.3 # instance variable can be changed of the class
m.company_name = "Microsoft" # instance variable
m.showDetals()

# Employee.showDetals(m) # this basically uppercase converted , as self
n = Employee("Nishi")
n.showDetals()

print(n.numberOfEmployees)