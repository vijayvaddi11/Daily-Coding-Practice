# class Solution:

#     def sortArray(self, n: List[int]) -> List[int]:
        # selection sort
        # len_n = len(n)
        # for i in range(len_n):
        #     min_val = i
        #     for j in range(i,len_n):
        #         if n[j]< n[min_val]:
        #             min_val = j
        #     n[i],n[min_val]=n[min_val],n[i]
        # return n


        #bubble sort
        # len_n = len(n) 
        # for i in range(len_n):
        #     for j in range(len_n-i-1):
        #         if n[j+1]< n[j]:
        #             n[j+1],n[j]=n[j],n[j+1]
        # return n


#
class Solution:

    def divide(self,n,l,r):
        #base case
        if l>=r:
            return 
        #reccursive case
        mid = (l+r)//2
        self.divide(n,l,mid)
        self.divide(n,mid+1,r)

        self.merge(n,l,mid,r)

    def merge(self,n,l,mid,r):
        a=[]
        b=[]

        for i in range(l,mid+1):
            a.append(n[i])
        for j in range(mid+1,r+1):
            b.append(n[j])
        
        i,j,k = 0,0,l
        while k <= r :
            if i == len(a):
                n[k]= b[j]
                k+=1
                j+=1
            elif j == len(b):
                n[k] = a[i]
                k+=1
                i+=1
            elif a[i]< b[j]:
                n[k] = a[i]
                k+=1
                i+=1
            else:
                n[k] = b[j]
                k+=1
                j+=1
        





    def sortArray(self, n: List[int]) -> List[int]:
        self.divide(n,0,len(n)-1)
        return n