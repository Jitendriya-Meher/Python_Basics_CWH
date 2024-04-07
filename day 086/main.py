# a = True
print(a:=True)

nums = [1,2,3,4,5]
while ( n:=len(nums) ) > 0 :
    print("pop() :",nums.pop())

foods = list()
while True:
    food = input("What food do you like? : ")
    if( food == "quit"):
        break
    foods.append(food)
print(foods)

foods = list()
while ( food:=input("What food do you like? : ")) != "quit":
    foods.append(food)
print(foods)