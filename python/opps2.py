class RailwayForm:
    formtype= "railway form"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        
application = RailwayForm()
application.name = "Deepanshu"
application.train = "Rajdhani express"
application.printdata()
