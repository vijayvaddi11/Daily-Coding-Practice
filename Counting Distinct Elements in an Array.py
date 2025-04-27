# Q35. Counting Distinct Elements in an Array



input_arr =  list(map(int,input().split()))

non_rep_arr =[]
for i in input_arr:
    if i not in non_rep_arr:
        non_rep_arr.append(i)
print(non_rep_arr)                
print(f"Counting Distinct Elements of given Array is : {len(non_rep_arr)}")        


    