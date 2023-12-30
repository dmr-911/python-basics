arr = [1, 2, 3]

print(dir(arr)) # show all methods

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 38)

print(p.__dict__)