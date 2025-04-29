# Q37. Count numbers of even and odd elements in an array

input_arr = list(map(int,input().split()))

even_num_in_arr = []
odd_num_in_arr = []

for num in input_arr:
    if num %2==0:
        even_num_in_arr.append(num)
    else:
        odd_num_in_arr.append(num)
        
print(f'even numbers in given array : {len(even_num_in_arr)} , {even_num_in_arr}')   
print(f'odd numbers in given array : {len(odd_num_in_arr)} , {odd_num_in_arr}')   

        