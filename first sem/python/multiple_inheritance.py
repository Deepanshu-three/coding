class Employee:
    company = "visa"
    
class Freelancer:
    company = "Fiverr"
    level = 0
    
    def upgrade(self):
        self.level = self.level + 1
    
class Programmer(Employee,Freelancer):
    name = "Rohit"
    
    
p = Programmer()
print(p.level)