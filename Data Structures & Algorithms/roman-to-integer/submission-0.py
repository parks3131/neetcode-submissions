class Solution:
    def romanToInt(self, s: str) -> int:
        romanHash = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        res = 0
        for i, sym in enumerate(s):
            if i + 1 < len(s) and romanHash[sym] < romanHash[s[i + 1]]:
                res-=romanHash[sym]
            else:
                res+=romanHash[sym]
        return res