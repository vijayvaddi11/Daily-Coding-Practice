class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(n)-1
        i=0
        while i <= r:
            if n[i]==2:
                n[r],n[i]=n[i],n[r]
                i-=1
                r-=1
            elif n[i]==0:
                n[l],n[i]=n[i],n[l]
                l+=1
            
            i+=1
                