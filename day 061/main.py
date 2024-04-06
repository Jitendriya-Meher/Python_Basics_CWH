class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Employee name is {self.name} and id is {self.id}")

class Programmer( Employee):
    def showLanguages(self):
        print(f"The default language is Python")

emp1 = Employee("Rohan Das",400)
emp1.showDetails()

emp1 = Programmer("Jitendriya Meher",2021)
emp1.showDetails()
emp1.showLanguages()