# Q36. Finding Repeating elements in an Array

def count_num_arr(input_arr, non_rep_arr):
    repeating_elements = []
    for i in non_rep_arr:
        count = 0
        for j in input_arr:
            if i == j:
                count += 1
        if count > 1:
            repeating_elements.append(i)
    print(f"Repeating elements in an Array: {repeating_elements}")        
            

input_arr = list(map(int, input().split()))

non_rep_arr = []
for i in input_arr:
    if i not in non_rep_arr:
        non_rep_arr.append(i)

 
count_num_arr(input_arr, non_rep_arr)
