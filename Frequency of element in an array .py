# Q34. Frequency of elements in an array

def num_repeat(number):
    li = []
    for num in number:
        if num not in li:
            li.append(num)
    return li      

input_arr = list(map(int, input().split()))
repeated_num = num_repeat(input_arr)

def count_of_number(input_arr, repeated_num):
    for i in repeated_num:
        count = 0
        for j in input_arr:
            if i == j:
                count += 1
        print(f"{i} is repeated {count} times")

count_of_number(input_arr, repeated_num)