class Person:
    # when constructor doesn't take any arguments it calls default constructor
    def __init__(self, name, occ) : # parameterized constructor
        # print("I am a constructor")
        self.name = name 
        self.occ = occ
        # self.name = name

    def info(self):
        print(f"{self.name} is {self.occ}")

a = Person("Mizan", "Developer")
b = Person("Rahad", "IT")
# c = Person(1, 2, 3)

a.info()
b.info()