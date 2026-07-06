class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s3 = s1
        s1 = list(s1)
        count = {}
        l=0
        for r,string in enumerate(s2):
            if string in s1:
                count[string]=1+count.get(string,0)
                if count[string]>s1.count(string):
                    if s2[r-1] == string:
                        count = {}
                        count[string] = 1
                    else:
                        while(l<r):
                            while(s2[l] not in count):
                                l+=1
                            if s2[l]==string:
                                count[s2[l]]-=1
                                l+=1
                                break
                            count[s2[l]]-=1
                            l+=1
            else:
                count = {}
            if sum(count.values()) == len(s3):
                    return True
        return False
