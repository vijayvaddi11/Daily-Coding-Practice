def insertion_sort(num):
    n= len(num)
    for i in range(1,n):
        for j in range(i,0,-1):
            if num[j-1]>num[j]:
                num[j-1],num[j]=num[j],num[j-1]
            else:
                break



num =[-3,9,4,-2,-3,2,6,-7,1]
insertion_sort(num)
print(num)
