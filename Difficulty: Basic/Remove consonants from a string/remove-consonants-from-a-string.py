#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        vowels=['a','e','i','o','u','A','E','I','O','U']
        st=''
        for i in s:
            if i in vowels:
                st+=i
        if st:
            return st
        else:
            return 'No Vowel'
            
