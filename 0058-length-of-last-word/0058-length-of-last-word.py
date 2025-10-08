class Solution:
    def stripRemover(self,s):
        n=len(s)
        start=0
        end=n-1

        while start<n and s[start]==" ":
            start+=1

        while end>0 and s[end]==" ":
            end-=1

        return s[start:end+1]    
            
          
    def lengthOfLastWord(self, s: str) -> int:
        remove_ex_spaces=self.stripRemover(s)
        n=len(remove_ex_spaces)
        count=0
        for i in range(n-1,-1,-1):
            if remove_ex_spaces[i]!=" ":
                count+=1
            else:
                break
        return count            
