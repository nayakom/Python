# <1> create a class programmer for strong information of few programmer working at microsoft.

class programmer:
    company = "Micosoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The Name Of The Programmer {self.name} And The Product Name Is {self.product}")

om = programmer("Om", "Python")
sheevi = programmer("Sheevi", "DJango")
om.getInfo()
sheevi.getInfo()


# <2> write a class calculator capable of finding squre, cube and squarroot of a number.

class calculator:
    def __init__(self, num):
        self.number = num

    def square (self):
        print(f"The value of {self.number} Square is {self.number **2}")

    def squareroot (self):
        print(f"The value of {self.number} SquareRoot is {self.number **0.5}")
    
    def cube (self):
        print(f"The value of {self.number} Cube is {self.number **3}")

a = calculator(10)
a.square()
a.squareroot()
a.cube()