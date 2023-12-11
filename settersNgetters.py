class myClass:
    def __init__(self, value):
        self._value = value 

    def show(self):
        print(f"Value is {self._value}")

    @property # decorator + getter , property is a default decorator
    def value(self):
        return self._value * 10
    @value.setter # decorator + setter
    def ten_value(self, value):
         self._value = value / 10
    

obj = myClass(14)
obj.ten_value = 133
print(obj.ten_value) # you can call a getter function as a variable

obj.show()