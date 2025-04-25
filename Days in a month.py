# Q24. Count the number of days in a given month of a year

def check_leapyear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False


month = int(input())    
year = int(input())   

if month in [1,3,5,7,8,10,12]:
    print('31')
elif month ==2:
    print('28' if check_leapyear(year)!=True else '29' )
else:
    print('30')
