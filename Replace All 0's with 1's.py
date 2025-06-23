# Q19. Replace All 0’s With 1 In A Given Integer


number = int(input())
str_num = str(number)
print(str_num.replace('0','1'))


'''
number = int(input())

str_num = str(number)

for i in range(0,len(str_num)):
    if str_num[i]=="0":
        str_num=str_num.replace('0','1')
print(str_num)        




number = input()
li_num = list(number)
output =""
for num in li_num:
    if num =='0':
        output+='1'
    else:
        str_num = str(num)
        output += str_num
print(int(output))'''
