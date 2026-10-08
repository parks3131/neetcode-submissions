class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == "":
            return True
        s_pointer, t_pointer = 0, 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer+=1
            t_pointer+=1
        return False if s_pointer < len(s) else True
            