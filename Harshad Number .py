# Q6.Harshad Number

number= input()
str_num = str(number)
add_of_numbers =0
for i in str_num:
    add_of_numbers+=int(i)
print(int(number)//add_of_numbers)