class Solution:
    def twoRepeated(self, arr):
        # code here
        ans=[]
        seen=set()
        for i in arr:
            if i not in seen:
                seen.add(i)
            else:
                ans.append(int(i))
        return ans