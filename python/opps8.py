class Employee:
      company = "google"
      
      def showdetails(self):
          print("This is an emoloyee")
        
        
class Programmer(Employee):
    language = "Pyhton"
    
    def getlanguage(self):
        print(f"The language is {self.language}")
        
        def showdetails(self):
            print("This is an programmer")
            

a = Employee()
a.showdetails()
p = Programmer()
print(p.company)
