from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        count=Counter(s)
        for i in s:
            if count[i]==1:
                return i
                break
        return -1    
    
    