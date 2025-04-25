# Q27. Find Smallest Element in an Array 

input_arr = list(map(int,input().split()))
min_element = input_arr[0]

for num in input_arr:
    if min_element>num:
        min_element=num
print(min_element)    

#print(min(input_arr)) 
   

