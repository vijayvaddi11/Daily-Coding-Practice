# Q19. Replace All 0’s With 1 In A Given Integer

number = input()
li_num = list(number)
output =""
for num in li_num:
    if num =='0':
        output+='1'
    else:
        str_num = str(num)
        output += str_num
print(int(output))