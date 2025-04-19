# Q2. Find Factorial of given input

input=int(input())
value_required=1
while input>=1:
    value_required*=input
    input-=1
print(value_required)