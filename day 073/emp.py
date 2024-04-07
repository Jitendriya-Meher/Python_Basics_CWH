class Employee:
    
    def __init__(self,name):
        self.name = name

    def __len__(self):
        l = 0
        for c in self.name:
            l=l+1
        return l
    
    def __str__(self):
        return f"The name of the Employee is {self.name} , str"
    
    def __repr__(self):
        return f"The name of the Employee is {self.name} , repr"

    def __call__(self):
        print(f"hii {self.name}")

if __name__ == '__main__':
    e1 = Employee("AMit")
    print(e1.name)
    print(len(e1))
    print(e1)

    e2 = Employee("AMit Meher")
    print(e2.name)
    print(len(e2))
    print(e2)
