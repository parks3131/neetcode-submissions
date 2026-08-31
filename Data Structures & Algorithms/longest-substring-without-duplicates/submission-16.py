class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                while l < r and s[l] != s[r]:
                    del hashmap[s[l]]
                    l+=1
                l+=1
            res = max(res, r - l + 1)
        return res
                


                        

