from functools import reduce

def cube(x):
    return x*x*x

print(cube(3))

l = (1, 2, 3, 4, 3)

# newl = []
# for num in l:
#     newl.append(cube(num))

#map
m = map(cube, l) # takes first argument as function, second argument a list
print(list(m))
# print(list(newl))

# filter 
def filter_function(a):
    return a>2
    
newfel = filter(filter_function, l)
newfel2 = filter(lambda x: x>2, l)
print(list(newfel))
print(list(newfel2))


# Reduce
sum = reduce(lambda x, y: x+y, l)
print(sum)