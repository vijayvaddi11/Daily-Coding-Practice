# Q28. Find the Smallest and largest element in an array 

input_arr = list(map(int,input().split()))
min_element = input_arr[0]
max_element = input_arr[0]

for num in input_arr:
    if num > max_element:
        max_element=num
    if num < min_element:
        min_element=num    

print(f"Smallest element in an array: {min_element}")        
print(f"Largest element in an array: {max_element}")   