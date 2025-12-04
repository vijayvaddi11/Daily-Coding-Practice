class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = defaultdict(int)
        # for i in nums:
        #     freq[i]+=1
        # max_key=0
        # max_val=0
        # for key,val in freq.items():
        #     if val>max_val:
        #         max_val=val
        #         max_key=key
        # return max_key


        #Boyer-Moore Voting Algorithm
        #tc- O(n) and sc- O(1)
        count=0
        res=0
        for i in nums:
            if count==0:
                res=i
                count=1
            elif res == i:
                count+=1
            else:
                count-=1
        return res
    
             