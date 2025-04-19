# cook your dish here
i=int(input())
value_required=1
while i>=1:
    value_required*=i
    i-=1
print(value_required)