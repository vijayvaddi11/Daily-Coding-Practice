# Q11.LCM Of Two Numbers
def factor(number):
    result=[]
    for i in range(1,number+1):
        if number%i==0:
            result.append(i)
    return result   

    
        
number1,number2 = map(int,input().split())
common_factors=[]
for num in factor(number1):
    if num in factor(number2):
        common_factors.append(num)
        
LCM = number1*number2//max(common_factors)

print(f'LCM of {number1} and {number2} is {LCM}')   