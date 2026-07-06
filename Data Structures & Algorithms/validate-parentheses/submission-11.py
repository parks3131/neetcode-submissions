class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"}":"{", ")":"(", "]":"["}
        res = []
        for i in s:
            if res and i in bracket:
                rem = res.pop()
                if rem == bracket[i]:
                    continue
                else:
                    return False
            else:
                res.append(i)
        return False if res else True