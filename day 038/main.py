class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def my_function():
    a = int(input("Enter any value between 5 and 9 : "))
    if( a<0):
        raise ValueError("Value should be positive")
    if(a<5  or a>9):
        raise  CustomError("Value should be between 5 and 9")
    
try:
    my_function()
    print("No errors found")
except CustomError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

