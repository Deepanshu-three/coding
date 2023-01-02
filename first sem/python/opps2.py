class RailwayForm:
    formtype= "railway form"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Time is {self.time}")  
        print("Hello")  
application = RailwayForm()
application.name = "Deepanshu"
application.train = "Rajdhani express"
application.time = "Today"
application.printdata()
