class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        Sum = 0
        for i in s[1:]:
            Sum+= abs(ord(i) - prev)
            prev = ord(i)
        return Sum
            