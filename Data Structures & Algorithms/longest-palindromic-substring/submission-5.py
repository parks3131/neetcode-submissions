class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""
        for i in range(len(s)):
            #odd
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if r - l + 1 > length:
                length = r - l +1
                res = s[l + 1:r]
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            if r - l + 1 > length:
                    length = r - l +1
                    res = s[l + 1:r]
        return res
            
                

        