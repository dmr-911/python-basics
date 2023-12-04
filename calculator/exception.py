a = input("Enter the number: ")

print(f"Multi table of {a} is")

try:
    for i in range(1, 11):
        print(f"{i} * {a} is = {i*int(a)}")
except Exception as e:
    print(e)

print("Hello outside try except")


try:
    for i in range(1, 11):
        print(f"{i} * {a} is = {i*int(a)}")
except ValueError:
    print("Value error")

except IndexError:
    print("Index error")

except SyntaxError:
    print("Syntax error")