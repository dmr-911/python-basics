class MyName:
    def __init__(self):
        self.__name = "Mizan" # it can be accessed from the class and it's sub classes
        self._age = 17 # it is a private convention, however python don't set bindings to single _ variables


name = MyName()
name.name = "Mizu"

print(name.name)
# print(name.__name) # cannot access private variable directly

# However it can be access indirectly
print(name._MyName__name) # with Name Mangling, it cannot be change accidentally, but can do it 

print(name.__dir__()) # to access all properties