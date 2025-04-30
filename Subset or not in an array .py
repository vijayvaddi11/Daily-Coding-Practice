# Q39. Check whether array is subset of another array or not 

a=[(1,2),(2,3)]
b = [(1,2),(2,3),(3,4),(4,5),(5,6)]

'''
len_a = len(a)
count=0
for i in a:
    for j in b:
        if i==j:
            count+=1
if count==len_a:
    print("yes")
else:
    print("no")
'''

'''
if all(nums in b for nums in a):
    print("yes a is sub set of b")
else:
    print("no a is not subset of b")
'''

# Performance at it peaks compared to nestnced for and all() fu
    
set_b = set(b)

if all(item in set_b for item in a):
    print("yes")
else: 
    print("no")