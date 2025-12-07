from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Brute Force Sc-(O(nlogn)) tc-(O(n))
        # freq = defaultdict(int)
        # for i in nums:
        #     freq[i]+=1

        # count = 1
        # ref=[]
        # for val in sorted(freq.values(), reverse=True):
        #     if count<=k:
        #         ref.append(val)
        #         count+=1
        
        # final_res=[]
        # for key,val in freq.items():
        #     if val in ref:
        #         final_res.append(key)
        # return final_res


        #Bucket Sort Solution
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        
        bucket = [[] for i in range(len(nums)+1)]

        for key,val in freq.items():
            bucket[val].append(key)
        
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res

        
        