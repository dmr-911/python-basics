class Math:
    def __init__(self, num) : 
        self.num = num

    def add_to_num(self, n) :
        self.num = self.num + n

    # Need to use in complex use cases 
    @staticmethod
    def add(a, b):
        return a + b
    

a = Math(5)

print(a.num)
a.add_to_num(5)
print(a.num)
print(a.add(5, 6))
print(Math.add(5, 6))