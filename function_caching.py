from functools import lru_cache
import time

@lru_cache(maxsize=None)
# when to use :

# when your function is taking more time than expected, use lru_cache
# it will return the value was executed before

def fx(n):
    time.sleep(5)
    return n * 5


print(fx(20), "done for 20")
print(fx(6), "done for 6")
print(fx(2), "done for 2")

print(fx(20), "done for 20")
print(fx(6), "done for 6")
print(fx(2), "done for 2")
print(fx(61), "done for 61")