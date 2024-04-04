def fact( n):
    if( n<=1):
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(2))
print(fact(5))
print(fact(10))

n = int(input("n = "))
print("factorial of n =",fact(n))