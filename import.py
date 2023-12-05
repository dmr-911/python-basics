import math # import all from math, we can use math.something like that
import math as m # renamed as m
from math import floor # import specific method
from mizan import mizan as z, m as y # rename specific methods too

from math import sqrt as s, pi as p # as to rename methods

# from math import * #not recommended process, but we can call all methods from this

print(math.floor(4.2323))
print(m.sqrt(4))

print(s(4))
print(floor(4.23223232)*p)


# print(dir(math), math.__doc__) # dir method to use what imported file returned

print(z(), y)