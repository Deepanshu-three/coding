class Person:
    country = "India"
    
    def takebreak(self):
        print("I am taking break")
        
class Employee(Person):
    
    def getsalary(self):
        print(f"salary is {self.salary}")
                