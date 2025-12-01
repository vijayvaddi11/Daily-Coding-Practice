class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using dict
        freq={}
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
                freq[i]=1
            else:
                freq[i]+=1
        
        for i in freq.values():
            if i>1:
                return True
        return False


