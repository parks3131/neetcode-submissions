class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need a hash table to keep track of distinct elements
        #we need an l and r to keep track of contigious and count the length
        #length is the maximum length

        l, r = 0, 0
        if len(s) == 0:
            return 0
        length = 1
        hashmap = defaultdict(int)
        while r < len(s):
            hashmap[s[r]]+=1
            while hashmap[s[r]] > 1:
                hashmap[s[l]]-=1
                l+=1
            if r-l+1 > length:
                length = r-l+1
            r+=1
        return length
        