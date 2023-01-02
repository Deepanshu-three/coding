"""
projecct number 16:

Design an application where user will input two dates.
1.	His/her date of birth in DD/MM/YY format.
2.	Current (Present day) date in DD/MM/YY format.
Your app will calculate and let the user know how many days that person survived in this world.
Note: Your calculation must be accurate and you have to consider leap and non-leap years separately.
(Student is free to decide the input and output layout for this mini project)

"""


from datetime import datetime

txt = "Wellcome"

x = txt.center(100)

print(x) 
print(" ---------->Today we are going to find out the number of days you survived in this world<----------")



# getting birthday from user in str format
str_d1 =  str(input("Enter your birthday in DD/MM/YYYY format: "))
print("\r")
print("\r")
# getting current date from user in str format
str_d2 = str(input("Enter current date in DD/MM/YYYY format: "))
print("\r")
print("\r")
# convert string to date object
d1 = datetime.strptime(str_d1, "%d/%m/%Y")
d2 = datetime.strptime(str_d2, "%d/%m/%Y")

# difference between dates in timedelta1
delta = d2 - d1
print(f'Congratulations you have successfully survived {delta.days} days in this world')



