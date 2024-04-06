class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"value = {self._value}")
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    @property
    def ten_value(self):
        return self._value*10
    
obj1 = MyClass(101)
print(obj1.value)
obj1.show()
print(obj1.ten_value)

obj1.value = 20
print(obj1.value)
obj1.show()
print(obj1.ten_value)