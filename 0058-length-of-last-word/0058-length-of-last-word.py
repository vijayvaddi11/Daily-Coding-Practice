class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=s.strip()
        f=[]
        u=""
        for i in j:
            if i==" ":
                f.append(u)
                u=""
            else:
                u+=i
        if u:
            f.append(u)

        return len(f[-1])  
