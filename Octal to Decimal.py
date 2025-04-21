# Q14.Octal To Decimal Conversion

octal_num=list(input())
count=0
power=0
for i in reversed(octal_num):
    val=int(i)*(8**power)
    count+=val
    power+=1
print(f'the Binary of input is {count}')    