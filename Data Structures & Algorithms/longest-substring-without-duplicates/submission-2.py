class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_s = list(s)
        window = []
        res = []

        for string in list_s:
            if string not in window:
                window.append(string)
            else:
                window= window[window.index(string)+1:]
                window.append(string)
            
            if len(res) < len(window):
                res = window[:]
        return len(res)

        