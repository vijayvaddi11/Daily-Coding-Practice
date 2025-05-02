# Star Pattern -4
'''
    ****
   ****
  ****
 ****
 
'''

for i in range(4):
    for j in range(4-i-1):
        print(" ",end="")
    for j in range(0,4):
        print("*",end="")
    print()