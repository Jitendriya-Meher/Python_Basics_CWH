class Math:

    def __init__(self,num):
        self.num = num

    def addToNum( self, n):
        self.num += n

    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result)

obj1 = Math(5)
print(obj1.num)
obj1.addToNum(11)
print(obj1.num)