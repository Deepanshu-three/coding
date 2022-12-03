class Number:
    def sun(self):
        return self.a+self.b

num = Number()    
num.a = 12
num.b = 32
s = num.sun()
print(s)