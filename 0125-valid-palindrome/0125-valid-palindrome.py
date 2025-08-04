class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(i.lower() for i in s if i.isalnum())
        initial=0
        final=len(s)-1
        def check(initial,final):
            if initial>=final:
                return True
            if s[initial]!=s[final]:
                return False
            return check(initial+1,final-1)   
        return check(initial, final)           