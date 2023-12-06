x = 4 #global x
print(x)

def hello():
    global x
    x= 4
    global y
    y= 6
    print(f"local x is {x}")

hello() # should execute before print
print(f"The global x is {x}")
print(f"The global y is {y}")