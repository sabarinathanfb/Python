class Computer:
    def __init__(self, name, proc):
        self.name = name
        self.proc = proc

class Phone(Computer):
    def __init__(self, name, proc):
        super().__init__(name, proc)

    def print(self):
        print(f"I am {self.name} and my Proc is {self.proc}")

class Laptop(Computer):
    def __init__(self, name, proc):
        super().__init__(name, proc)

    def print(self):
        print(f"I am {self.name} and my Proc is {self.proc}")

class Tablet(Computer):
    def __init__(self, name, proc):
        super().__init__(name, proc)

    def print(self):
        print(f"I am {self.name} and my Proc is {self.proc}")

# Creating objects
obj1 = Phone("Iphone", 15)
obj2 = Laptop("Mac", "A1")
obj3 = Tablet("Ipad", 12)

# Calling print methods
obj1.print()
obj2.print()
obj3.print()
