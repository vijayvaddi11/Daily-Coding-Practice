class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using sorting
        # res = defaultdict(list)

        # for i in strs:
        #     sortedI = "".join(sorted(i))
        #     res[sortedI].append(i)
        # return list(res.values())


        #hashmap
        res=defaultdict(list)

        for i in strs:
            count = [0]*26
            for s in i:
                count[ord(s)-ord('a')]+=1
            res[tuple(count)].append(i)
        return list(res.values())

