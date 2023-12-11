def greet(fn):  # Decorator function that takes a function as an argument
    def mfx():  # Inner function that adds functionality to the original function
        print("Good morning")  # Prints a greeting message
        fn()  # Calls the original function passed as an argument
        print("Thanks for using this function")  # Prints a closing message
    return mfx  # Returns the inner function

@greet  # Decorator: Calls greet function with hello function as an argument
def hello():
    print("Hello")

hello()  # Calls the decorated hello function
# We can also write like this : greet(hello)(), but the way shown is much simpler
