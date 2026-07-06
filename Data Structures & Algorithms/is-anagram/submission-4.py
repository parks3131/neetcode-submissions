class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = list(s)
        t_s = list(t)
        if len(l_s) != len(t_s):
            return False
        for i in range(len(l_s)):
            if l_s[i] in t_s:
                t_s.remove(l_s[i])
                
        if len(t_s) == 0:
            return True
        else:
            return False