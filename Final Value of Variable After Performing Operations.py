#2011. Final Value of Variable After Performing Operations
'''There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0'''


operations=["--X","X++","X++"]
X=0
for i in operations:
  if i=='X++' or i=='++X':
    X+=1
  else:
    X-=1
print(X)