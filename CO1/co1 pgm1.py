year=int(input("enter a year "))
if (year%400==0) or (year%4 and year%1001==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")
