class Animal :
    def __init__(self, name) -> None:
        self.name = name

    def sound(self):
        print(f"Animal {self.name} makes sound!")


class Dog(Animal):
    def __init__(self) -> None:
        self.name = "Dog"

    def sound(self) : # method overriding
        print(f"Dog sound is barking!")

a = Animal("Dog")
d = Dog()

print(a.sound())
print(d.sound())