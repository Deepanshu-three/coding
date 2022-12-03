class Employee:
     company = "Google"
     

harry = Employee()
rajni = Employee()
print(harry.company)
print(rajni.company)

Employee.company="Youtube"
print(harry.company)
print(rajni.company)
