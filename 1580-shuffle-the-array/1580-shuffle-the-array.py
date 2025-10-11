class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)

        nums1=[]
        for i in range(n//2):
            nums1.append(nums[i])


        nums2=[]
        for i in range(n//2,n):
            nums2.append(nums[i])
    
        result=[]
        for i in range(n//2):
            result.append(nums1[i])
            result.append(nums2[i])
        return result       