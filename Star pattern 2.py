# Star Pattern -2
'''
   ****
   *  *
   *  *
   ****
'''

for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print('*', end="")
        else:
            print(' ',end="")
    print()        
    
    
    
    
    
    
    
    
# for i in range(5):
#     for j in range(5):
#         if i in [1,2,3] and j in [1,2,3]:
#         #if 1 <= i <= 3 and 1 <= j <= 3:    
#                 print(' ',end='')
#         else:        
#             print('*', end='')
#     print('')        