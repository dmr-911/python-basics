class Animal :
    def __init__(self, name) -> None:
        self.name = name

    def sound(self):
        print(f"Animal {self.name} makes sound!")


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("Dog")
        self.category = "Dog"

    def sound(self) : # method overriding
        super().sound()
        print(f"{self.category} sound is barking!")

class Shepard(Dog):
    def __init__(self) -> None:
        self.name = "Shepard"
        super().__init__()

    def show(self):
        super().sound()
        print(f"{self.name} {self.category} is barking!")
s = Shepard()

s.sound()

print(Shepard.mro())