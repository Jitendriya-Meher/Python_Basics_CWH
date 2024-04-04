tup = ( 1, 2, 5, 6, "abs")
print(tup, type(tup))

tup1 = ( 1)
print(tup1, type(tup1))

tup2 = ( 1,)
print(tup2, type(tup2))

# tup[0] = 100

print(tup[0])
print(tup[-1])

print(tup[1:5:2])

if "abs" in tup:
    print("abs is present")
else:
    print("abs is not present")