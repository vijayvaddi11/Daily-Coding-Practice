# Q7. factors of a number

num = int(input())
factors=[]
for _ in range(1,num+1):
    if num%_ ==0:
        factors.append(_)
print(factors)        