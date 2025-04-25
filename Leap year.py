# Q23. If a given Year is Leap Year

year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print('leap year')
else:
    print('Not a leap year')