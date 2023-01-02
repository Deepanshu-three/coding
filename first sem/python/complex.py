class Complex:
    def __init__(self,i,j):
        self.real = i
        self.imaginary = j
        
    def __add__(self,c):
        return Complex(self.real + c.real,self.imaginary+c.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
    
a = Complex(3,5)
b = Complex(4,6)
print(a+b)