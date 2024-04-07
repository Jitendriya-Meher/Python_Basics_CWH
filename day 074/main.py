class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,r):
        self.r = r
        super().__init__(r,r)

    def area(self):
        return 3.1416 * super().area()
    
rect = Shape(3,5)
print(rect.area())

cir = Circle(5)
print(cir.area())