# Q3. Fibonacci Series upto nth term

input= int(input())
li=[0,1]
li_num =len(li)-1
li_num
while li_num<=input:
    if li_num >=2:
        newLi = (li[li_num-1])+(li[li_num-2])
        li.append(newLi)
        
   
    li_num+=1
print(li)
