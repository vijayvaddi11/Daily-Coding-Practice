# Q8. Abundant Number

num = int(input())
factors =[]
for i in range(1,num):
    if num%i == 0:
        factors.append(i)
        
sum_factors=sum(factors)        
if sum_factors > num:
    print("It's an Abundant Number")
else:
    print("It's not an Abundant Number")
