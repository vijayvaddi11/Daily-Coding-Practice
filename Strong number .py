# cook your dish here
i = int(input())
strI=str(i)
li=[]

for num in strI:
    fact =1
    num=int(num)
    while num>=1:
        fact*=num
        num-=1
    li.append(fact)    

print('It is a Strong Number') if sum(li)==i else print('It is not a Strong Number')
    
    
 