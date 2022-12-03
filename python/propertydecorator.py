class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryafterincrement(self):
        return self.salary * self.increment

    @salaryafterincrement.setter
    def salaryaferincrement(self,sai):
        self.increment = sai/self.salary
        

e = Employee()
print(e.salaryaferincrement)
e.salaryaferincrement = 2000
print(e.increment)
