# def bubble_sort(num):
#     n=len(num)
#     flag=True
#     while flag:
#         flag=False
#         for i in range(1,n):
#             if num[i-1]>num[i]:
#                 flag=True
#                 num[i-1],num[i]=num[i],num[i-1]


# def insertion_sort(num):
#     n=len(num)
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if num[j-1]>num[j]:
#                 num[j-1],num[j]=num [j],num[j-1]

            

def selection_sort(num):
    n=len(num)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if num[j]<num[min_index]:
                min_index=j
        num[i],num[min_index]=num[min_index],num[j]        
                
            


num=[-5,4,2,-2,4,8,1,3]
# bubble_sort(num)
# insertion_sort(num)
selection_sort(num)
print(num)
