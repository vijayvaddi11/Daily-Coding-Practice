# Q2. Find Factorial of given input

input=int(input())
value_required=1

if input>=1:
    while input>=1:
        value_required*=input
        input-=1
    print(value_required)
elif input==0:
    print('0')
elif input<0:
    print('factorial of a negative number is not defined')
