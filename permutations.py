# Q16.Permutations In Which N People Can Occupy R Seats In A Classroom

def factorials(number):
    factorial= 1
    for i in range(1,number+1):
        factorial*=i
    return factorial
    
num1,num2 = map(int,input().split()) 
N=factorials(num1)
R=factorials(num1-num2)

print(f'Total possible arrangements: {N//R}')