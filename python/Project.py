"""
projecct number 16:

Design an application where user will input two dates.
1.	His/her date of birth in DD/MM/YY format.
2.	Current (Present day) date in DD/MM/YY format.
Your app will calculate and let the user know how many days that person survived in this world.
Note: Your calculation must be accurate and you have to consider leap and non-leap years separately.
(Student is free to decide the input and output layout for this mini project)

"""


# some decorations
txt = "Wellcome"
x = txt.center(100)

print(x)
print("\r")
print("\r")

txt1 = "---------->Today we are going to find out the number of days you survived in this world<----------" 
y = txt1.center(100)
print(y)
print("\r")
print("\r")


#taking input from the user in the form DD/MM/YYYY
a = input("Enter your birthday in DD/MM/YYYY format: ").split("/")
print("\r")
b = input("Enter the present date in DD/MM/YYYY format: ").split("/")
print("\r")
print("\r")

# getting int of year
by = a[2]
birthy = int(by)
py = b[2]
presenty = int(py)

# defin a function to check the leap year in giving range of years, and getting no of days in year
def year(a,b):
    yearday = 0
    for year in range(birthy,presenty ):
        if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
            yearday+=366
        else:
            yearday+=365
    return yearday

daysofyear = year(birthy,presenty)


# getting int of month
bm = a[1]
bmonth = int(bm)
pm = b[1]
pmonth = int(pm)

# swapping month to get the bigger month
if bmonth > pmonth:
    bmonth,pmonth = pmonth,bmonth

# define a function to get the number of days in month
def month(a,b):
    monthday = 0
    for month in range(bmonth,pmonth):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            monthday+=31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            monthday+=30
        else:
            monthday+=28
    return monthday

daysofmonth = month(bmonth,bmonth)


# getting int of days
bd = a[0]
bdate = int(bd)
pd = a[0]
pdate = int(pd)

# getting no of days between days given
daysofdays = abs(bdate - pdate)


# adding the number of days 
totalnumberofdays = daysofdays+daysofmonth+daysofyear

# printing the total number of days
print(f'Congratulations you have successfully survived {totalnumberofdays} days in this world')
print("\r")
print("\r")