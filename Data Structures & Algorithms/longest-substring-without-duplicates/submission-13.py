class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need a hash table to keep track of distinct elements
        #we need an l and r to keep track of contigious and count the length
        #length is the maximum length

        hashmap = defaultdict(int)
        l, r = 0, 0
        length = 0
        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                while s[l] != s[r]:
                    del hashmap[s[l]]
                    l+=1
                l+=1
            length = max(length, r - l + 1)    
            r+=1
        return length
