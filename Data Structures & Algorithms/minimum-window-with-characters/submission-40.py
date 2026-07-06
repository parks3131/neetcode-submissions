class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #move your right until have = 3
        alph_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        r = l = have = 0
        res = [-1,-1]
        length = float("inf")

        while r < len(s):
            alph_dict[s[r]]+= 1
            if s[r] in t_dict and alph_dict[s[r]] <= t_dict[s[r]]:
                have+= 1
            while have == len(t):
                if r-l+1 < length:
                    res = [l,r]
                    length = r-l+1
                if s[l] in t_dict and alph_dict[s[l]] == t_dict[s[l]]:
                    have-= 1
                alph_dict[s[l]]-= 1
                l +=1
            r+= 1
        if res == [-1,-1]:
            return ""
        l,r = res
        return s[l:r+1]





        