class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr( cls, string ):
        # return cls(string.split('-')[0],int(string.split('-')[1]))
        name,salary = string.split("-")
        return cls(name,int(salary))

e1 = Employee("Harry",12000)
print(e1.name)
print(e1.salary)

str = "John-1200"
e2 = Employee.fromStr(str)
print(e2.name)
print(e2.salary)