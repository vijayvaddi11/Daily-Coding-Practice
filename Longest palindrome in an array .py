# Q34. Longest Palindrome in an Array

arr = list(map(int,input().split()))

palindrome=[]
for i in arr:
    rev =str(i)[::-1]
    if str(i) == rev:
        palindrome.append(int(rev))
if not  palindrome:
    print('there are no palindromes in this arrray')
else:    
    print(f"the max palindrome in an array is: {max(palindrome)}")


'''
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
 '''
