# Q4. Perfect Number

number = int(input())
divisors =[]
for i in range(1,number):
    if number%i==0:
        divisors.append(i)
if sum(divisors)==number:
    print('It is a Perfect Number') 
else:
    print('It not is a Perfect Number')
