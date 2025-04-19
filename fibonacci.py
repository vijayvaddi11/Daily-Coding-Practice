# cook your dish here
x= int(input())
li=[0,1]
li_num =len(li)-1
li_num
while li_num<=x:
    if li_num >=2:
        newLi = (li[li_num-1])+(li[li_num-2])
        li.append(newLi)
        
   
    li_num+=1
print(li)
