'''
Project 21:
Your task is to find if it is possible to cut the cake in the below mentioned ways for a given value of N.
Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
The given cake can be cut in following three ways: 
•	Cut the cake into N equal pieces.
•	Cut the cake into N pieces of any size.
•	Cut the cake into N pieces such that no two of them are equal.

'''
txt="<=========..............Welcome..............==========>"
print("\r")

print(txt.center(100))

print("\r")
print("Today we are here to cut the cake for u remember the cut will in the straight line going through the center.")
print("\r")

n = int(input("Enter how many pieces you want from a cake: "))
print("\r")
print("\r")


while(True):
    print(f'''Choose how you want to cut the cake for {n} number of pieces.
      
      * Choose 1 to cut the cake into {n} number of pieces of equal size.
      * Choose 2 to cut the cake into {n} number of pieces of any size.
      * Choose 3 to cut the cake into {n} number of pieces in which no two pieces are equal.
      * Choose 4 to exit the code''')
    print("\r") 
    a = int(input("Enter your choice:"))
    
    print("\r")
    print("\r")
    if a<=4 and a>0:
        
        #Case 1: To cut the cake into n number of equal pieces
        if a==1:
            if n%2==0:
                print(f"Total number of cut required for {n} number of pieces are: {n//2} and angle between 2 cuts must be {360/n} degrees.")
            else:
                print(f"It is not possible to cut the cake for {n} equal pieces because {n} is a odd number and you can cut cake into straight line through center.")




        #Case2: cut the cake into n pieces of any size.
        if a==2:
            if n%2==0:
                print(f"Total number of cut required for N number of pieces are: {n//2} and you can decide the angle as you required.")
            else:
                print(f"It is not possible to cut the cake for {n} equal pieces because {n} is a odd number and you can cut cake into straight line through center.")


        #Case3:Cut the cake into N pieces such that no two of them are equal.
        if a == 3:
            print("Sorry, you cannot cut the cake in straight line passing through the center in which no two sides are equal.")
            
        #Exiting the code
        
        if a==4:
            print("Thanks for using my code. Have a great day!")
            exit()
    else:
        print("Invalid Choice please choose correctly.")
    print("\r")
    print("\r")