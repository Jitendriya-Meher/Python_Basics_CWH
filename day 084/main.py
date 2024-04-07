import time

def usingWhile():
    i=0
    sum=0
    while( i<50000):
        i=i+1
        sum += i

def usingFor():
    sum=0
    for i in range(50000):
        sum += i

t1 = time.time()
print(t1)
usingWhile()
print("while loop =",time.time() - t1)


t1 = time.time()
print(t1)
usingFor()
print("for loop =",time.time() - t1)

# time.sleep(2)
# print("this will wait for 2 seconds")

t = time.localtime()
print(t)
formated_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formated_time)