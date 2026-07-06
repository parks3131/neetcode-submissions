class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count, window = {}, {}
        l = 0
        res, res_length = [-1,-1], float("infinity")
        for c in range(len(t)):
            count[t[c]] = 1 + count.get(t[c],0)
        need = len(count)
        have = 0
        for r in range(len(s)):
            if s[r] in count:
                window[s[r]] = 1 + window.get(s[r],0)
                if window[s[r]] == count[s[r]]:
                    have+=1
            while(have == need):
                if r-l+1 < res_length:
                    res = [l,r]
                    res_length = r-l+1
                if s[l] in count:
                    window[s[l]]-=1
                    if window[s[l]] < count[s[l]]:
                        have-=1
                l+=1
        
        l,r = res
        return s[l:r+1] if res_length != float("infinity") else ""
                
            

        