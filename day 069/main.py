class Employee:
    company = "Jiksss..."
    def show(self):
        print(f'name = {self.name}\ncompany = {self.company}')

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = 'jiten'
e1.show()

e1.changeCompany("Jikkss...New")
e1.show()

e2 = Employee()
e2.name = 'Amit'
e2.show()
