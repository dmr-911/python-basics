class Employee : 
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

mizan = Employee("Mizan", 420)
m = Programmer("M", 840, "C++")

print(m.id, m.name)