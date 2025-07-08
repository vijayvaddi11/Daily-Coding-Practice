# def sort(num):
#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j]>num[j+1]:
#                 temp=num[j]
#                 num[j]=num[j+1]
#                 num[j+1]=temp
    


def bubble_sort(num):
    n=len(num)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if num[i-1]>num[i]:
                flag=True
                num[i-1],num[i]=num[i],num[i-1]
                
                



num=[-5,3,2,1,-3,-3,7,2,2,-2]
# sort(num)
# print(num)
bubble_sort(num)
print(num)
