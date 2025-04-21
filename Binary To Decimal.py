# Q13.Binary To Decimal Conversion

binary=list(input())
count=0
power=0
for i in reversed(binary):
    val=int(i)*(2**power)
    count+=val
    power+=1
print(f'the octal num of input is {count}')    