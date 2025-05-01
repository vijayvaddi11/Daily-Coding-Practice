# Q40 .Checking a character is a vowel or consonant

input = input()

input_len= len(input)

vowels = ['a','e','i','o','u']

if input_len ==1:
    if input in vowels:
        print(input, "is a vowel")
    else:
        print(input, "is not a vowel")
else:
    print("input must be a single digit")