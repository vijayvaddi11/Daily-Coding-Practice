class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #tc-O(n) sc-O(1)
        result=0
        for num in nums:
            result^=num
        return result




        # tc-O(n), sc-O(n)
        
        # freq={}
        # seen=set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        #         freq[i]=1
        #     else:
        #         freq[i]+=1
        

        # for key,value in freq.items():
        #     if value==1:
        #         return key
