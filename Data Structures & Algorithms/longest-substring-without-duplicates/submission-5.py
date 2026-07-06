class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        alphabets = set()
        for r in range(len(s)):
            while s[r] in alphabets:
                alphabets.remove(s[l])
                l+=1
            if s[r] not in alphabets:
                alphabets.add(s[r])
                res = max(res,r-l+1)
        return res
            
            




        