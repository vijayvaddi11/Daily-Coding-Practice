class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start =0
        count=0
        for i in range(1,len(nums)):
            #same 
            if nums[start]==nums[i]:
                #first repeate
                if count<1:
                    start+=1
                    count+=1
                    nums[start]=nums[i]
                #second or more repete                    
                elif count>=1:
                    count+=1
            #new element        
            else:
                count=0
                start+=1
                nums[start]=nums[i]
        return start+1             