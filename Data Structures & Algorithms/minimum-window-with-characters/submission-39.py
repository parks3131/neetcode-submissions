class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #move your right until have = 3
        alph_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        r = l = have = 0
        res = []
        length = float("inf")

        while r < len(s):
            alph_dict[s[r]]+= 1
            if s[r] in t_dict and alph_dict[s[r]] <= t_dict[s[r]]:
                have+= 1
            while have == len(t):
                if r-l+1 < length:
                    if not res: 
                        res.append([l,r])
                    else:
                        res[0][0] = l
                        res[0][1] = r
                    length = r-l+1
                if s[l] in t_dict and alph_dict[s[l]] == t_dict[s[l]]:
                    have-= 1
                alph_dict[s[l]]-= 1
                l +=1
            r+= 1
        if not res:
            return ""
        start = res[0][0]
        end = res[0][1]
        return s[start:end+1]





        