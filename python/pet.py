class Animal:
    animaltype = "Mammel"

class Pet:
    colour = "white"
    
class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")
        
d = Dog()
d.bark()