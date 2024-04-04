def average2no( a,b):
    avg = (a+b)/2
    print("The Average is",avg)

def average2noDef( a=1,b=3):
    avg = (a+b)/2
    print("The Average is",avg)

def averageNno( *nums):
    print(nums,type(nums))
    sum = 0
    for x in nums:
        sum += x
    print("Average is",sum/len(nums))
    

average2no(2,3)
average2noDef()
average2noDef(b=7)
average2noDef(b=17, a=78)

averageNno(1,2,3,4,5)
averageNno(1,2,3,4)