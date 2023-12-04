try :
    l = [1, 2, 3, 4]
    i = int(input("Enter the index : "))
    print(l[i])

except Exception as e:
    print(e)

finally: # I will always execute
    print("I can be throw anyone anywhere!")

    