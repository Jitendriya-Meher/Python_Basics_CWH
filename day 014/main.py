age = int(input("Enter your age : "))

# if else statement
if( age > 18):
    print("Yes")
    print("You can drive yourself")
else:
    print("No")
    print("You can't drive yourself") 


# if elif statement
if( age < 10):
    print("Your are a kid")
elif( age < 20):
    print("Your are a teenager")
elif( age < 60):
    print("Your are a adult")
else:
    print("Your are too old")

# nested if elif statement
if( age > 18):
    print("Yes")
    print("You can drive yourself")
    if( age > 60):
        print("You are too old for a driver")
    else:
        print("Have a save ride")
else:
    print("No")
    print("You can't drive yourself")
    if( age < 10):
        print("Grow up first")