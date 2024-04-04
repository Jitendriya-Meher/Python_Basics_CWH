l = [ 1,89,7,80,76]
print(l)

l.append(19)
print(l)

l.reverse()
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

print(l.index(1))

print(l.count(1))

m = l
m[0]=0
print(l)

p = l.copy()
p[0] = 100
print(l)

l.insert(1,899)
print(l)

l.extend(m.copy())
print(l)

k = l + m
print(k)