class Calculator:
    def __init__(self,number):
         self.number = number
         
    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")
        
    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number **(1/2)}")
        
    def cube(self):
        print(f"the value of {self.number} cube is {self.number**3}")
        
a = Calculator(5)
a.square()
a.squareroot()
a.cube()