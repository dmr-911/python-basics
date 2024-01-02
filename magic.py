from typing import Any


class Employee :
    def __init__(self, name) :
        self.name = name
    def __len__(self): # returns the length of something
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self) -> str: # returns a string
        return f"The name of the employee is {self.name}, returned from str"
    
    def __repr__(self) -> str: # returns a string
        return f"The name of the employee is {self.name}, returned from repr"
    
    def __call__(self, *args: Any, **kwds: Any) -> Any: # used for direct class call as a function
        print("Hey I am good")

e = Employee("Mizan")
# print(e) # default call value
print(len(e))
print(str(e))
print(repr(e))
e() # for call method