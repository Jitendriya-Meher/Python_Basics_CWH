class Employee:
    
    companyName = "Jiksss..."
    noOfEmp = 0

    def __init__(self,name):
        self.name = name 
        self.raiseAmt = 0.02
        Employee.noOfEmp += 1

    def showDetails(self):
        print(f"employee name is {self.name} and raiseAmt is {self.raiseAmt}, company = {self.companyName}, companySize = {self.noOfEmp}")

emp1 = Employee("jiten")
emp1.showDetails()

emp1.raiseAmt = 0.05
emp1.companyName = "Jiksss... India"

Employee.showDetails(emp1)

emp2 = Employee("Amit")
emp2.showDetails()

Employee.companyName = "Jiksss India"

emp1.showDetails()
emp2.showDetails()