# a = True
# print(a:=False)

# numbers = [1, 2, 3, 4, 5]

# while(n := len(numbers)) > 0:
#     print(numbers.pop())
# print(numbers)


foods = list()

# without walrus operator 
while True:
    food = input("What food do you like? ")
    if food == "quit":
        break
    foods.append(food)

# with walrus operator
while (food:=input("what do you want ? ")) != "quit":
    foods.append(food)


print(foods)