class Person:
    name = "Jiten"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation} and networth is {self.networth}.")

p1 = Person()
print(p1.name, p1.networth)
p1.info()

p1.name = "Jitendriya"
p1.networth = 20
print(p1.name, p1.networth)
p1.info()

p2 = Person()
p2.name = "Amit"
p2.info()