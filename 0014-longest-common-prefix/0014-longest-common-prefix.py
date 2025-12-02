class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res=''

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i== len(s) or s[i] != strs[0][i]:
        #             return res
        #     res+=strs[0][i]
        # return res


        #vertical scanning
        # smallest = min(strs, key=len)
        # res=''

        # for i in range(len(smallest)):
    
        #     current = smallest[i]
    
        #     for s in strs:
        #         if s[i]!= current:
        #             return res
        #     res+=current
        # return res
        


        #Horizontal scanning
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].startswith(prefix)==False:
                prefix = prefix[:-1]
        return prefix
