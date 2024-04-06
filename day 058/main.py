class Person:
    # name = "jiten"
    # occ = "Developer"

    # def __init__(self):
    #     print("default constructor called")

    def __init__(self,name="jiten",occ="Software Developer"):
        print(f"Parameteriesed constructor called")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

p1 = Person()
p1.info()
p1.name = "jitendriya"
p1.occ = "CEO"
p1.info()

p2 = Person("Amit","Dev.")
p2.info()