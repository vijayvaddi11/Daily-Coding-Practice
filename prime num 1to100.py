# Q21. find Prime Numbers between 1 to100.

def factor(number):
    factors=[]
    for i in range(1,number+1):
        if number%i==0:
            factors.append(i)
    return factors 
        
number=100
prime=[]
for i in range(1,number+1):
    if len(factor(i))==2:
        prime.append(i)
print(prime)        

