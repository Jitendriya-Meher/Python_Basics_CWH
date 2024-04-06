
def greet( fx):
    def mfx(*tup, **dict):
        print("Good Morning.")
        fx(*tup, **dict)
        print("Thanks for using this function.\n")
    return mfx

@greet
def hello():
    print("Hello, world!")

@greet
def add(a,b):
    print(f"{a} + {b} = {a+b}")


hello()
add(3,8)