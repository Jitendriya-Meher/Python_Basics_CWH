info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

for (key, value) in info.items():
    print(f"The value corresponding to the key {key} is {value}") 

print(info['name'])
print(info.get('age'))

print(info.keys())

print(info.values())

print(info.items())