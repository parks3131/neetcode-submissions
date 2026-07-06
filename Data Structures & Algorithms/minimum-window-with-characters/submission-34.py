class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, length = 0, 0, len(s)
        res = ""
        if len(t) > len(s):
            return res
        if len(s) == len(t) or len(s) == len(t) == 1:
            if s == t:
                return t

        track = []
        dict_t = {}

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        while l < len(s):
            if s[l] in t:
                track.append(l)
            l += 1
        
        if not track:
            return res
        l = track.pop(0)


        while r <= len(s):
            r = l
            temp = dict_t.copy()
            while sum(temp.values()) != 0 and r < len(s):
                if s[r] in temp and temp[s[r]] > 0: 
                    temp[s[r]] -= 1
                r += 1
            if sum(temp.values()) == 0 and r - l <= length:
                length = r - l
                res = s[l:r]
            if not track:
                break
            l = track.pop(0)

        return res