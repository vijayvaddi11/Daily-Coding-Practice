# Q38. Find whether arrays is disjoint or not using Python 

input_arr1 = list(map(int,input().split()))
input_arr2 = list(map(int,input().split()))

count=0
for i in input_arr1:
    if i in input_arr2:
        count+=1
if count >=1:
    print(" Not Disjoint")
else:
    print("Disjoint")



'''arr1 = set(map(int, input("Enter elements of first array: ").split()))
arr2 = set(map(int, input("Enter elements of second array: ").split()))

if arr1.isdisjoint(arr2):
    print("Disjoint")
else:
    print("Not Disjoint")'''
