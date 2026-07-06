class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        substr = ""
        while(l<len(strs[0])):
            for i in range(1,len(strs)):
                if l == len(strs[i]) or strs[0][l] != strs[i][l]:
                    return substr
            substr+=strs[0][l]
            l+=1
        return substr
        



            