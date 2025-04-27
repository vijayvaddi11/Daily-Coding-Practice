# Q34. Longest Palindrome in an Array

def palindrome(arr):
    palindrome=[]
    for num in arr:
        str_num = str(num)
        reverse_num = str_num[::-1]
        if str_num == reverse_num:
            palindrome.append(num)
    return palindrome        
            

input_arr = list(map(int,input().split()))

palindrome_arr = palindrome(input_arr)

print(f'Longest Palindrome : {max(palindrome_arr)}')

