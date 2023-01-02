class Train:
    def __init__(self, name , fare ,seat):
        self.name = name 
        self.fare =fare
        self.seat = seat
        
    def getststus(self):
        print(f"The number of seats in your train is {self.seat}")
        print(f"the number of seats avialable in your train is {self.seat}")
        
    def fareinfo(self):
        print(f"fare of tour train is {self.fare}")
        
    def bookticket(self):
        if (self.seat>0):
            print(f"your ticket is booked and your seat number is {self.seat}")
            self.seat = self.seat - 1
            
            
t = Train("Howrah Mail",90,300)
t.getststus()
t.bookticket()
t.bookticket()
t.getststus()