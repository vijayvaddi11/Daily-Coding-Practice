class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 
        freq1={}
        for i in s:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i]+=1
        
        freq2={}
        for j in t:
            if j not in freq2:
                freq2[j]=1
            else:
                freq2[j]+=1
        
        for key in freq1.keys():
            if key not in freq2 or freq1[key]!=freq2[key]:
                return False
        return True
        
        

        


        