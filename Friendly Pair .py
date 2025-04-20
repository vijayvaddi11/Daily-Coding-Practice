# Q9.Friendly Pair

#{(sum of factors of first number) ÷ first number} = {(sum of factors of second number) ÷ second number} 

def sum_factors(number):
    sum_factors=0
    for i in range(1,number):
        if number%i==0:
            sum_factors+=i 
    return sum_factors    

number1,number2 = map(int,input().split())


if sum_factors(number1)/ number1 == sum_factors(number2) / number2:
    print("Yes, they are a friendly pair")
else:
    print("no, they are not a friendly pair")
    
    