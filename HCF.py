# Q10. find HCF of Two Numbers

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

print(f'HCF of {number1} and {number2} is {max(common_factors)}')   
