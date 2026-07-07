class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash = {}
        if len(s) == 0:
            return 0
        l, r = 0, 1
        res = 1
        char_hash[s[l]] = 1
        while r < len(s):
            if s[r] in char_hash:
                while l < r :
                    del char_hash[s[l]]
                    if s[l] == s[r]:
                        l+=1
                        break
                    l+=1
            char_hash[s[r]] = 1
            res = max(res, r - l + 1)
            r+=1
        return res
                        

