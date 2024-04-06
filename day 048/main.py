x = 4
print(x)

def hello():
    x = 5
    print(f"local x = {x}")
    print("HELLO")

print(f"global x = {x}")
hello()
print(f"global x = {x}")