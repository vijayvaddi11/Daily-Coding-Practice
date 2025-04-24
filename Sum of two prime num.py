# Q20.Can A Number Be Expressed As A Sum Of Two Prime Numbers? 

def factor(number):
    if number<2:
        return False
    factors=[]    
    for num in range(1,number+1):
        if number%num==0:
            factors.append(num)
        
    return  len(factors)==2

            
number = int(input())
prime_li=[]
for i in range(1,number+1):
    if factor(i)==True:
        prime_li.append(i)
print(prime_li)      


try:
    for i in range(len(prime_li)):
        for j in range(i,len(prime_li)):
            if prime_li[i]+prime_li[j]==number:
                print(f"{prime_li[i]} + {prime_li[j]} = {number}")
except :
    print("cannot be expressed as the sum of two prime numbers")