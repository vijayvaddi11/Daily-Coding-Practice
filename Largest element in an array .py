# Q26.Find Largest element in an array

input_arr = list(map(int,input().split()))
max_element = input_arr[0]
for num in input_arr:
    if num > max_element:
        max_element = num
print(max_element)        

#print(max(input_arr))

#or
a=sorted(input_arr)
len_arr = len(input_arr)
print(a[len_arr-1])
