class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        max_key=0
        max_val=0
        for key,val in freq.items():
            if val>max_val:
                max_val=val
                max_key=key
        return max_key
    
             