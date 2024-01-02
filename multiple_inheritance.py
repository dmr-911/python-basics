class Employee : 
    def __init__(self, name) -> None:
        self.name  = name

    def show(self):
        print(f"The name is {self.name}")
class Dancer : 
    def __init__(self, dance) -> None:
        self.dance = dance

    def show(self):
        print(f"The name is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance) -> None:
        self.dance = dance
        self.name = name

de = DancerEmployee("Munni", "Classic")

de.show()

print(DancerEmployee.mro())