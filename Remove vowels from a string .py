# Q41 .Remove Vowels from a String

input_str = input()
vowels =['a','e','i','o','u','A','E','I','O','U']
str_without_vowels=""
for i in input_str:
    if i not in vowels:
        str_without_vowels+=i
        
print('Remove vowels in input string :',str_without_vowels)