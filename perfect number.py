# cook your dish here
number = int(input())
divisors =[]
for i in range(1,number):
    if number%i==0:
        divisors.append(i)
print('It is a Perfect Number') if sum(divisors)==number else print('It not is a Perfect Number')
