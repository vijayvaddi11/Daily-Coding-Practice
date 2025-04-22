# Q18. Addition of two fractions

numerator1,denominator1,numerator2,denominator2 = map(int,input().split())

if denominator1==denominator2:
    print((numerator1+numerator2)/denominator1)
else:
    print(((numerator1*denominator2)+(numerator2*denominator1))/(denominator1*denominator2))
    