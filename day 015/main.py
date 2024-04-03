import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

hour = int(time.strftime('%H'))

if( hour < 12 ):
    print("Good Morning")
elif( hour < 19 ):
    print("Good Afternoon")
else:
    print("Good Night")