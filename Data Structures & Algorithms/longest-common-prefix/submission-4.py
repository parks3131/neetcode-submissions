class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        start = strs[0]
        res = ""
        for i in range(len(start)):
            prefix = start[:i+1]
            for j in range(1,len(strs)):
                if prefix != strs[j][0:i+1]:
                    return res
            res = prefix
        return res