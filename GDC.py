# Q12.GCD of Two Numbers (Greatest Commom Divisor)

def divisiors(number):
    divisiors = []
    for i in range(1,number+1):
        if number%i==0:
            divisiors.append(i)
    return divisiors        


num1,num2 = map(int,input().split())
common_divisiors=[]
for i in divisiors(num1):
    if i in divisiors(num2):
        common_divisiors.append(i)
print(f'GCD of {num1} and {num2} is {max(common_divisiors)}')