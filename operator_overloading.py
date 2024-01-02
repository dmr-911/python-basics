class Vector :
    def __init__(self, i , j , k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"{self.i}i, {self.j}j, {self.k}k"
    
    def __add__(self, x):
        # return  f"{self.i + x.i}i, {self.j + x.j}j, {self.k + x.k}k" # returned as string, but we want vector
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)



v1 = Vector(3, 5, 6)
v2 = Vector(3, 5, 6)

print(v1)
print(v1 + v2)
print(type(v1+v2))