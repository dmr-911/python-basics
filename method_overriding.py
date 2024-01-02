class Shape :
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()

rec = Shape(10,5)

cir = Circle(5)

print(rec.area())
print(cir.area())