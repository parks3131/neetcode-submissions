class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need a hash table to keep track of the elements
        #count to store the longes
        #move r until we get a repeated and move the left until s[l] == s[r]

        store_hash = {}
        l,r = 0, 0
        count = 0
        while r<len(s):
            if s[r] not in store_hash:
                store_hash[s[r]] = 1
                r+=1
                count = max(count,r-l)
            else:
                while s[r] in store_hash:
                    del store_hash[s[l]]
                    l+=1
        return count
