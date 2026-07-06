class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we need a l and r pointer so that the elements inbetween them is distict characters
        #we also wanna keep track of the shortest string which has the every required character
        #so to keep track we need a hash table
        t_hash = defaultdict(int)
        for i in t:
            t_hash[i]+=1
        want = len(t_hash)
        have = 0
        hash_map = defaultdict(int)
        l, r = 0, 0
        length = float("inf")
        result = ""

        while r < len(s):
            if s[r] in t_hash:
                hash_map[s[r]]+=1 
                have = have + 1 if hash_map[s[r]] == t_hash[s[r]] else have
            while have == want:
                if length > r-l+1:
                    length = r-l+1
                    result = s[l:r+1]

                if s[l] in t_hash:
                    hash_map[s[l]]-=1
                    if hash_map[s[l]] < t_hash[s[l]]:
                        have-=1
                l+=1
            r+=1
        
        return result

        
            


