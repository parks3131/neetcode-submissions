class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_check = []
        res, count, l = 0, 0, 0
        for r in range(len(s)):
            if s[r] not in list_check:
                list_check.append(s[r])
                count+=1
            else:
                res = max(res,count)
                while(l<=r):
                    if s[l] == s[r]:
                        l+=1
                        break
                    else:
                        count-=1
                        list_check.remove(s[l])
                    l+=1
        return max(res,count)
                    


        