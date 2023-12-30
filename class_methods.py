class Employee :
    company = "Apple"
    def show(self):
        print(f"The name of company is {self.company}")

    @classmethod # add classmethod decorator
    def change_company(cls, newCompany): # it takes first param as class, second as you want
        cls.company = newCompany

emp = Employee()
emp.show()
emp.change_company("Tesla")
emp.show()
print(Employee.company)