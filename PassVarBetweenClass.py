class Class1:
    def __init__(self):
        self.var = "Hello"

class Class2:
    def __init__(self, var):
        self.var = var

c1 = Class1()
c2 = Class2(c1.var)
print(c2.var)  # Output: Hello
