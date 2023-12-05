# Factorial 
def factorial(n):
    if(n == 0 or n==1):
        return 1
    return n * factorial(n-1)

print(factorial(6))


# Fibonacci sequence
# f0=0
# f1=1
# f2 = f1+f0
# fn = fn(n-1) + fn(n-2)
def fibonacci(n):
        # Check if n is 0
    # then it will return 0
    if n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))