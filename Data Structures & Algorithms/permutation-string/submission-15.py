class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        count = {}
        l=0
        for r,string in enumerate(s2):
            if string in s1:
                count[string]=1+count.get(string,0)
                if count[string]>s1.count(string):
                    while(l<=r):
                        if s2[l]==string:
                            count[s2[l]]-=1
                            l+=1
                            break
                        count[s2[l]]-=1
                        l+=1
            else:
                count = {}
                l=r+1
            if sum(count.values()) == len(s1):
                    return True
        return False
