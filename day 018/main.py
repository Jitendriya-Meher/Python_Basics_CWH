x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is',x)

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if number < 0:
        break
