class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we need a l and r pointer so that the elements inbetween them is distict characters
        #we also wanna keep track of the shortest string which has the every required character
        #so to keep track we need a hash table
        count_t = Counter(t)
        l = r = 0
        have = 0
        length = float("inf")
        want = len(count_t)
        hashmap = defaultdict(int)
        substring = ""

        while r < len(s):
            hashmap[s[r]]+=1
            if s[r] in count_t and hashmap[s[r]] == count_t[s[r]]:
                have+=1
            while have == want:
                if r-l+1 < length:
                    substring = s[l:r+1]
                    length = r-l+1
                hashmap[s[l]]-=1
                if s[l] in count_t and hashmap[s[l]] < count_t[s[l]]:
                    have-=1
                l+=1
            r+=1
        return substring
        
            


