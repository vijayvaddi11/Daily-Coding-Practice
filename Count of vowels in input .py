# Q41 .Count the number of vowels

input_str = input()
vowels =['a','e','i','o','u','A','E','I','O','U']
count_of_vowels = 0
for i in input_str:
    if i in vowels:
        count_of_vowels+=1
print('count of vowels in input string :',count_of_vowels)