class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_a = s.split()
        return len(list_a[-1])
        