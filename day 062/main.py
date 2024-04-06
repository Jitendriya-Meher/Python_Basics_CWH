class Employee:
    def __init__(self):
        self.name = "Jiten" # public
        self.__id = 2021 # private

emp1 = Employee()
print(emp1.name)

# print(emp1.__id)
print(emp1._Employee__id)

# print(emp1.__dir__())

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 