# Q29. Find Second Smallest Element in an Array

input_arr = list(map(int,input().split()))
input_arr.sort()
len_arr = len(input_arr)
print(input_arr[len_arr-2])