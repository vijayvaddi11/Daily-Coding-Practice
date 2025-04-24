# Q22.Calculate number of digits in an integer



def count_digit(number):
    str_number= str(number)
    count=0
    for i in str_number:
        count+=1
    return count    




number= int(input())
print(f'Number of digits in given input string : {count_digit(number)}')