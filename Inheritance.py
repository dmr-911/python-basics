class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"{self.id} is {self.name}")

class Programmer(Employee): # programmer has all the attributes of employee has
    def showLang(self):
        print(f" The Default language is python")

a = Employee("Mizan", 1)
a2 = Programmer("Hola", 2) 
a.show()
a2.show()
a2.showLang()