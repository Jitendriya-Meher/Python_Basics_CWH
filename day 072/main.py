class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("This is the child method parent method.")
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def info(self):
        print("name: " + self.name + " id: " + self.id)

class Programmer(Employee):
    def __init__(self,name,id,language):
        # self.name = name
        # self.id = id
        super().__init__(name,id)
        self.language = language

    def info(self):
        print("name: " + self.name + " id: " + self.id + " language: " + self.language)

rohan = Employee("Rohan","123ef")
rohan.info()

amit = Programmer("Amit","123efg","c++")
amit.info()