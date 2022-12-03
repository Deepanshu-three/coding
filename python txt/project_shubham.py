'''
Project 21:
Your task is to find if it is possible to cut the cake in the below mentioned ways for a given value of N.
Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
The given cake can be cut in following three ways: 
•	Cut the cake into N equal pieces.
•	Cut the cake into N pieces of any size.
•	Cut the cake into N pieces such that no two of them are equal.

'''

n = int(input("Enter how many cut you want for a cake: "))
r = int(input("Enter the cake radius: "))
# case1: Cut the cake in n equal pieces.
area_of_cake = 3.14 * (r**2)
if n<180:
    area_of_each_arc = area_of_cake/n*2
    no_of_cuts = n*2
    angle_of_cake = 360/(n*2)
    print("The cake can be cut into",no_of_cuts,"number of equal pieces of area","{:.2f}".format(area_of_each_arc),
          "unit squared of angle",angle_of_cake,"degrees")
else:
    print("The number of cuts in the cake is not possible")
