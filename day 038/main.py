class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def my_function():
    a = int(input("Enter any value between 5 and 9 : "))
    if(a<5  or a>9):
        raise  CustomError("Value should be between 5 and 9")
    else:
        raise CustomError("Number is valid")


try:
    my_function()
except CustomError as e:
    print(e)

