class C2dvac:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f"{self.icap}i+ {self.jcap}j"
    
class C3dvac(C2dvac):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap =k 
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
v2d = C2dvac(1,3)
v3d = C3dvac(1,9,7)
print(v2d)
print(v3d)