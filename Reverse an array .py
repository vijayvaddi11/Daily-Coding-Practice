# Q31. Reverse an Array

input_arr = list(map(int,input().split()))

#print(input_arr[::-1])

len_arr = len(input_arr)
reversed_arr = []
for num in range(1,len_arr+1):
    reversed_arr.append(input_arr[-num])
print(reversed_arr)    
    