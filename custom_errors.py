a = int(input("Enter any value between 5 and 9 : "))


# Defining custom exception
class CustomError(Exception):
    # pass;
    def __init__(self, message):
        print(message)
        self.message = message

if(a<5 or a > 9):
    raise CustomError("Invalid Input HEllo 8888")
