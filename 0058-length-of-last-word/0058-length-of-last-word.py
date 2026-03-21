class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = s.strip()
        count=0
        for i in n[::-1]:
            if i == " ":
                break
            count+=1
        return count
