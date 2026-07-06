class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        for i in s:
            if i == "(":
                count+=1
                res.append(i)
            elif i == ")" and count > 0 :
                count-=1
                res.append(i)
            elif i != ")" :
                res.append(i)
        
        for i in range(len(res)-1,-1,-1):
            if count>0 and res[i] == "(":
                count-=1
                res.pop(i)
            if count == 0:
                break
        return "".join(res)


        