# Q5. Find Strong Nuber or Not

input_num = int(input())
str_num=str(input_num)
li=[]

for num in str_num:
    fact =1
    num=int(num)
    while num>=1:
        fact*=num
        num-=1
    li.append(fact)    

if sum(li)==input_num:
    print('It is a Strong Number') 
else:
    print('It is not a Strong Number')
    
    
 