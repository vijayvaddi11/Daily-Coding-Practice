class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!= len(t):
        #     return False 
        # freq1={}
        # for i in s:
        #     if i not in freq1:
        #         freq1[i]=1
        #     else:
        #         freq1[i]+=1
        
        # freq2={}
        # for j in t:
        #     if j not in freq2:
        #         freq2[j]=1
        #     else:
        #         freq2[j]+=1
        
        # for key in freq1.keys():
        #     if key not in freq2 or freq1[key]!=freq2[key]:
        #         return False
        # return True


        if len(s)!= len(t):
            return False 

        freq={}

        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for j in t:
            if j in freq:
                freq[j]-=1
            else:
                return False

        for val in freq.values():
            if val<0 or val>0:
                return False
        return True
        
        #using single hashmap more optimal than double 
        #space comp-O(n)
        #time Comp-O(n)
        

        


        