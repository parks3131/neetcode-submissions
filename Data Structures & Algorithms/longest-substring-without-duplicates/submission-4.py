class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, count = 0, 0
        list_alphabet = []
        for r in range(len(s)):
            while (s[r] in list_alphabet):
                list_alphabet.pop(0)
                count-=1
            if s[r] not in list_alphabet:
                list_alphabet.append(s[r])
                count+=1
                res = max(count,res)
        return res
            
            




        