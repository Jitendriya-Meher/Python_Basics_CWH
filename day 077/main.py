class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,other):
        # return f"{self.i+other.i}i + {self.j+other.j}j + {self.k+other.k}k" 
        return Vector(self.i+other.i , self.j+other.j ,  self.k+other.k)
    
    def __sub__(self,other):
        return Vector(self.i-other.i , self.j-other.j ,  self.k-other.k)
    
v1 = Vector(1,2,3)
print(v1)

v2 = Vector(4,5,6)
print(v2)

print(type(v1+v2))

print((v1+v2))
print((v1-v2))