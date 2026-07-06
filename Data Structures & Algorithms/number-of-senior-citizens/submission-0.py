class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            age = int(i[-4:-2]) # -2 will not be included
            res = res + 1 if age > 60 else res
        return res
            

        