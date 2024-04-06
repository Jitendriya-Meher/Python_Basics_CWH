a = 5
b = 5

print("AAA") if (a>b) else print("BBB")

# else is mandatory
print("A if") if (a>b) else ""

print("A") if (a>b) else print("==") if (a==b) else print("B")

c = 123 if (a>b) else 456
print(c)